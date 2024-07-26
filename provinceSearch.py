import os
from collections import defaultdict


def should_ignore(line, ignore_words):
    return any(word in line for word in ignore_words)


def search_number_in_file(file_path, number, ignore_words, number_counts):
    results = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if should_ignore(line, ignore_words):
                continue
            words = line.split()
            for word in words:
                try:
                    value = float(word)
                    if value > number:
                        # Collect the context lines
                        start = max(i - 1, 0)
                        end = min(i + 2, len(lines))
                        context = lines[start:end]
                        results.append((file_path, i + 1, context))
                        number_counts[(file_path, value)] += 1
                except ValueError:
                    continue
    return results


def search_in_directories(directories, number, ignore_words):
    number_counts = defaultdict(int)
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.txt', '.csv', '.log', '.json', '.xml')):  # Add or modify file types as needed
                    file_path = os.path.join(root, file)
                    results = search_number_in_file(file_path, number, ignore_words, number_counts)
                    if results:
                        for file_path, line_number, context in results:
                            print(f"\nFile: {file_path}")
                            print(f"Line number: {line_number}")
                            for idx, line in enumerate(context):
                                print(f"{idx + line_number - 1}: {line.strip()}")

    # Print found numbers and their counts
    print("\nSummary of found numbers:")
    for (file_path, value), count in number_counts.items():
        print(f"File: {file_path}, Number: {value}, Count: {count}")


if __name__ == "__main__":
    directories = [
        #'common/scripted_triggers',
        #'common/scripted_localisation',
        #'common/scripted_guis',
        #'common/ai_focuses',
        #'common/ai_strategy_plans',
        #'common/ai_strategy'
        'events',
        'common/decisions',
        'common/national_focus',
        'common/on_actions',
        'common/scripted_effects',
        'map'
    ]
    number = float(input("Enter the number to search for: "))
    ignore_words = ['manpower', 'log', 'state_population', 'variable', 'add_fuel', 'random', 'has_unit_leader',
                    'country_event', 'factor', 'remove_unit_leader', 'size', 'value', 'days_remove', 'days', 'amount',
                    'days_mission_timeout', 'BAT_labourers', 'id', 'add_equipment_to_stockpile', 'infantry_equipment',
                    'option', '#', 'legacy_id']
    search_in_directories(directories, number, ignore_words)