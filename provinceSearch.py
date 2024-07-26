import os

def should_ignore(line, ignore_words):
    return any(word in line for word in ignore_words)

def search_number_in_file(file_path, number, ignore_words):
    results = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if should_ignore(line, ignore_words):
                continue
            if any(float(word) > number for word in line.split() if word.replace('.', '', 1).isdigit()):
                # Collect the context lines
                start = max(i - 1, 0)
                end = min(i + 2, len(lines))
                context = lines[start:end]
                results.append((file_path, i + 1, context))
    return results

def search_in_directories(directories, number, ignore_words):
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.txt', '.csv', '.log', '.json', '.xml')):  # Add or modify file types as needed
                    file_path = os.path.join(root, file)
                    results = search_number_in_file(file_path, number, ignore_words)
                    if results:
                        for file_path, line_number, context in results:
                            print(f"\nFile: {file_path}")
                            print(f"Line number: {line_number}")
                            for idx, line in enumerate(context):
                                print(f"{idx + line_number - 1}: {line.strip()}")

if __name__ == "__main__":
    directories = [
        'events',
        'common/decisions',
        'common/national_focus',
        'common/on_actions',
        'common/scripted_effects'
    ]
    number = float(input("Enter the number to search for: "))
    ignore_words = ['manpower', 'log', 'state_population', 'variable', 'add_fuel', 'random', 'has_unit_leader',
                    'country_event', 'factor', 'remove_unit_leader', 'size', 'value', 'days_remove', 'days', 'amount',
                    'days_mission_timeout', 'BAT_labourers', 'id', 'add_equipment_to_stockpile', 'infantry_equipment']
    search_in_directories(directories, number, ignore_words)
