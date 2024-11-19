#!/usr/bin/python3
import argparse
import os
import re
import glob
import sys

#Please don't look at this file. It's a horrible frankenstein of Yard1's province recycler, my own code, and ChatGPT (I'm sorry, please forgive me).
#Usage is identical to Yard1's province recycler minus the file name. This script changes province IDs in the history and map folders so they can be recycled.
#It also updates the victory point loc for both english and russian.

list1 = []


def read_file(name, ids):

    print("Reading file " + name + "...")
    with open(name, "r") as f:
        lines = f.read().splitlines()

    for id in ids:
        found_idx = -1
        for idx, line in enumerate(lines):
            if line.startswith(str(id) + ";"):
                found_idx = idx
                break

        if found_idx < 0:
            print("ID %s not found!" % str(id))
            continue
        print("Found ID %s at line %s" % (str(id), str(found_idx)))

        split_last_line = lines.pop().split(";", 1)
        list1.append(int(split_last_line[0]))
        split_found_line = lines[found_idx].split(";", 1)
        split_found_line[1] = split_last_line[1]
        lines[found_idx] = ';'.join(split_found_line)

    print("Writing to file " + name + "...")
    with open(name, "w") as f:
        f.writelines(str(line) + "\n" for line in lines)


#############################
parser = argparse.ArgumentParser(description='Recycle given province IDs in the given definition.csv file.')
parser.add_argument('ids', nargs='+', type=int,
                    help='Province IDs to find - space separated list')

args = parser.parse_args()

read_file('map\\definition.csv', args.ids)
list2 = args.ids

# Define the directories to search
directories_to_search = ['map', 'history\\states', 'history\\units']

# Define the specific files to search
specific_files = [
    'localisation\\english\\victory_points_l_english.yml',
    'localisation\\russian\\victory_points_l_russian.yml',
]

# Define the number lists (example data; replace with your actual lists)
#list1 = [20718, 20717, 20716, 20715, 20714, 20713, 20712, 20711, 20710, 20709]  # Numbers to find
#list2 = [2249, 2251, 2260, 2270, 2275, 2277, 2296, 2302, 2303, 2304]  # Corresponding replacement numbers
#print("Hello?")
#print(list1)
#print(list2)

# Check that the lists are of equal length
if len(list1) != len(list2):
    print("Error: The two lists must have the same number of elements.")
    exit()

# Create a mapping of numbers to replace
replacement_map = dict(zip(list1, list2))

# Regex patterns for the specific block types
provinces_block_pattern = re.compile(r'provinces\s*=\s*\{([^\}]*)\}', re.DOTALL)
numbered_block_pattern = re.compile(r'(\d+)\s*=\s*\{([^\}]*)\}', re.DOTALL)
victory_points_pattern = re.compile(r'victory_points\s*=\s*\{([^\}]*)\}', re.DOTALL)
location_pattern = re.compile(r'location\s*=\s*(\d+)')

# Regex to match numbers (not part of other numbers)
def create_regex(number):
    return re.compile(rf'(?<!\d){number}(?!\d)')

# Function to replace numbers in a block of text
def replace_numbers_in_block(text, replacement_map, vp=False):
    modified = False
    for old_number, new_number in replacement_map.items():
        regex = create_regex(old_number)
        if vp and regex.search(text):
            print(f"victory point {old_number} {new_number}")
        if regex.search(text):
            modified = True
        text = regex.sub(str(new_number), text)
    return text, modified

# Function to replace numbers in the file
def replace_numbers_in_file(filepath, replacement_map, encoding):
    try:
        with open(filepath, 'r', encoding=encoding) as file:
            content = file.read()
        #if encoding == 'utf-8-sig':
            #print(content)
        # Special handling for specific files
        filename = os.path.basename(filepath)
        is_railways_file = filename in ['railways.txt', 'adjacencies.csv', 'victory_points_l_english.yml', 'victory_points_l_russian.yml']
        is_special_case_file = filename in ['rocketsites.txt', 'airports.txt']
        is_buildings_file = filename == 'buildings.txt'

        modified = False

        if is_railways_file:
            # Replace whole numbers only in railways.txt, adjacencies.csv, and specific localisation files
            for old_number, new_number in replacement_map.items():
                regex = create_regex(old_number)
                if regex.search(content):
                    modified = True
                content = regex.sub(str(new_number), content)
        elif is_buildings_file:
            # Replace last numbers in each line in buildings.txt
            lines = content.splitlines()
            new_lines = []
            for line in lines:
                parts = line.split(';')
                if parts:
                    last_number = parts[-1].strip()
                    if last_number.isdigit() and int(last_number) in replacement_map:
                        parts[-1] = str(replacement_map[int(last_number)])
                        modified = True
                new_lines.append(';'.join(parts))
            content = '\n'.join(new_lines)
        else:
            # Replace numbers within 'provinces={...}' blocks
            def replace_in_provinces_block(match):
                block_content = match.group(1)
                new_content, was_modified = replace_numbers_in_block(block_content, replacement_map)
                nonlocal modified
                modified = modified or was_modified
                return f'provinces={{{new_content}}}'

            content = provinces_block_pattern.sub(replace_in_provinces_block, content)

            if is_special_case_file:
                # Replace numbers within numbered block {...} in rocketsites.txt and airports.txt
                def replace_in_numbered_block(match):
                    key = match.group(1)
                    block_content = match.group(2)
                    new_content, was_modified = replace_numbers_in_block(block_content, replacement_map)
                    nonlocal modified
                    modified = modified or was_modified
                    return f'{key}={{{new_content}}}'

                content = numbered_block_pattern.sub(replace_in_numbered_block, content)
            else:
                # Handle numbered block for history/states
                def replace_in_numbered_block(match):
                    key = match.group(1)
                    block_content = match.group(2)
                    new_key = key
                    nonlocal modified
                    for old_number, new_number in replacement_map.items():
                        if new_key == str(old_number):
                            new_key = str(new_number)
                            modified = True
                            break
                    new_content, was_modified = replace_numbers_in_block(block_content, replacement_map)
                    modified = modified or was_modified
                    return f'{new_key}={{{new_content}}}'

                content = numbered_block_pattern.sub(replace_in_numbered_block, content)

                # Replace numbers within 'victory_points = {...}' blocks and log the change
                def replace_in_victory_points_block(match):
                    block_content = match.group(1)
                    new_content, was_modified = replace_numbers_in_block(block_content, replacement_map, vp=True)
                    nonlocal modified
                    modified = modified or was_modified
                    return f'victory_points={{{new_content}}}'

                content = victory_points_pattern.sub(replace_in_victory_points_block, content)

                # Replace numbers in 'location = ...' lines for history/units
                def replace_in_location_line(match):
                    old_number = match.group(1)
                    new_number = replacement_map.get(int(old_number), old_number)
                    if str(old_number) != str(new_number):
                        nonlocal modified
                        modified = True
                    return f'location = {new_number}'

                content = location_pattern.sub(replace_in_location_line, content)

        # Only write the modified content back if there were changes
        if modified:
            with open(filepath, 'w', encoding=encoding) as file:
                file.write(content)
            print(f"Processed: {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

# Walk through the directories
for directory in directories_to_search:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt') or file == 'adjacencies.csv':  # Process .txt files and adjacencies.csv
                file_path = os.path.join(root, file)
                replace_numbers_in_file(file_path, replacement_map, 'utf-8')

# Process specific localisation files
for specific_file in specific_files:
    if os.path.isfile(specific_file):
        replace_numbers_in_file(specific_file, replacement_map, 'utf-8-sig')

print("Number replacement completed.")