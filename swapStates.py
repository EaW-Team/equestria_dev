import os
import re

# Define the directories to search
directories_to_search = ['map', 'history\\states']

# Define the number lists (example data; replace with your actual lists)
list1 = [20728, 20727, 20726, 20725, 20724, 20723, 20722, 20721, 20720, 20719]  # Numbers to find
list2 = [1003, 1799, 1895, 1904, 1935, 1940, 1942, 2112, 2140, 2143]  # Corresponding replacement numbers

# Check that the lists are of equal length
if len(list1) != len(list2):
    print("Error: The two lists must have the same number of elements.")
    exit()

# Create a mapping of numbers to replace
replacement_map = dict(zip(list1, list2))

# Regex patterns for the specific block types
provinces_block_pattern = re.compile(r'provinces=\{([^\}]*)\}', re.DOTALL)
keyed_block_pattern = re.compile(r'(\[\d+\])=\{\s*([^}]+)\s*\}', re.DOTALL)
bracketed_numbers_pattern = re.compile(r'\{([^\}]*)\}', re.DOTALL)


# Regex to match numbers (not part of other numbers)
def create_regex(number):
    return re.compile(rf'(?<!\d){number}(?!\d)')


# Function to replace numbers in a block of text
def replace_numbers_in_block(text, replacement_map):
    for old_number, new_number in replacement_map.items():
        regex = create_regex(old_number)
        text = regex.sub(str(new_number), text)
    return text


# Function to replace numbers in the file
def replace_numbers_in_file(filepath, replacement_map):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Special handling for specific files
        filename = os.path.basename(filepath)
        is_railways_file = filename == 'railways.txt'
        is_special_case_file = filename in ['rocketsites.txt', 'airports.txt']

        if is_railways_file:
            # Replace whole numbers only in railways.txt
            for old_number, new_number in replacement_map.items():
                regex = create_regex(old_number)
                content = regex.sub(str(new_number), content)
        elif is_special_case_file:
            # Replace numbers within any curly bracket block
            def replace_in_bracketed_block(match):
                block_content = match.group(1)
                return f'{{{replace_numbers_in_block(block_content, replacement_map)}}}'

            content = bracketed_numbers_pattern.sub(replace_in_bracketed_block, content)
        else:
            # Replace numbers within 'provinces={...}' blocks
            def replace_in_provinces_block(match):
                block_content = match.group(1)
                return f'provinces={{{replace_numbers_in_block(block_content, replacement_map)}}}'

            content = provinces_block_pattern.sub(replace_in_provinces_block, content)

            # Replace numbers within '[any number]={...}' blocks
            def replace_in_keyed_block(match):
                key = match.group(1)
                block_content = match.group(2)
                return f'{key}={{ {replace_numbers_in_block(block_content, replacement_map)} }}'

            content = keyed_block_pattern.sub(replace_in_keyed_block, content)

        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Processed: {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")


# Walk through the directories
for directory in directories_to_search:
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):  # Only process .txt files
                file_path = os.path.join(root, file)
                replace_numbers_in_file(file_path, replacement_map)

print("Number replacement completed.")