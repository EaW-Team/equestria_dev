import glob
import re
import os
import logging


# Utility classes
class TestRunner:
    """
    Test class that contains full filepath to mod folder
    Initialized via fixture, accepts 2 args, both passed via pytest console:
    -username: pass via --username=my_username, it is system user name in which docs mod is located
    -mod_name: pass via --mod_name=my_modname

    Example: C:\\Users\\username\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\mod_name\\
    """
    def __init__(self, username: str, mod_name: str) -> None:
        self.username = username
        self.mod_name = mod_name
        if os.name == "nt":
            self.full_path_to_mod = f"C:\\Users\\{username}\\Documents\\Paradox Interactive\\Hearts of Iron IV\\mod\\{mod_name}\\"
        elif os.name == "posix":
            self.full_path_to_mod = f"/Users/{username}/Documents/Paradox Interactive/Hearts of Iron IV/mod/{mod_name}/"


class FileOpener:
    '''
    Test class that hosts common file functions like opening text files
    '''
    @classmethod
    def open_text_file(cls, filename: str, lowercase: bool = True) -> str:
        """Opens and returns text file in utf-8-sig encoding

        Args:
            filename (str): text file to open
            lowercase (bool): defines if returned str is converted to lovercase or not. Default - True

        Raises:
            FileNotFoundError: if file is not found

        Returns:
            str: contents of the text file converted to lowercase
        """
        try:
            with open(filename, 'r', encoding='utf-8-sig') as text_file:      # 'utf-8-sig' is mandatory for UTF-8 w/BOM
                if lowercase:
                    return text_file.read().lower()
                else:
                    return text_file.read()
        except Exception as ex:
            logging.error(f"Skipping the file {filename}, {ex}")
            raise FileNotFoundError(f"Can't open the file {filename}")


class DataCleaner:
    @classmethod
    def skip_files(cls, files_to_skip: list, filename: str) -> bool:
        """Skip files in the list

        Args:
            files_to_skip (list): list with filenames
            filename (str): list with filenames

        Returns:
            bool: True if file should be skipped
        """
        for file in files_to_skip:
            if file in filename:
                return True


# Logging starts here
def format_logging_events(username, mod_name):
    """Add logging to events

    Args:
        username (_type_): windows username
        mod_name (_type_): mod folder name
    """
    test_runner = TestRunner(username, mod_name)
    filepath_to_events = f'{test_runner.full_path_to_mod}events\\'
    files_to_skip = ['Pilot', 'LaR', 'Nuke', ' - Vanilla']
    false_positives = []
    options_event_logging_args = {
        "country_event": "[GetLogInfo]",
        "state_event": "[GetLogInfo]",
        "unit_leader_event": "[GetLogInfo]",
    }
    immediate_event_logging_args = {
        "country_event": "[GetLogInfo]",
        "state_event": "[GetLogInfo]",
        "unit_leader_event": "[GetLogInfo]",
        "news_event": "[GetLogInfo]",
    }
    event_id = []
    # 1. Event logging - options
#    for event_type, logging_loc in options_event_logging_args.items():
#        for filename in glob.iglob(filepath_to_events + '**/*.txt', recursive=True):
#            if DataCleaner.skip_files(files_to_skip=files_to_skip, filename=filename):
#                continue
#
#            text_file = FileOpener.open_text_file(filename, lowercase=False)
#            pattern_event = '^' + event_type + r' = \{(.*?)^\}'
#            pattern_matches = re.findall(pattern_event, text_file, flags=re.DOTALL | re.MULTILINE)
#            if len(pattern_matches) > 0:
#                dict_with_str_to_replace_event = dict()
#                for event in pattern_matches:
#                    print(event_id)
#                    event_id = re.findall(r'^(?:\t|    )id = ([^ \n\t]+)', event, flags=re.MULTILINE)[0]
#
#                    hidden_event = "donotlog" in event
#                    if event_id in false_positives or hidden_event:
#                        continue
#
#                    options = re.findall(r'(^\toption = \{.*?^\t\})', event, flags=re.DOTALL | re.MULTILINE)
#
#                    for index, option in enumerate(options):
#                        dict_with_str_to_replace_option = dict()
#                        has_any_logging = "log =" in option
#                        has_data_logging = 'log = "KR_Event_Logging' in option
#                        option_name = re.findall(r'^\t\tname = ([^ \n\t]+)', option, flags=re.MULTILINE)[0] if '\n\t\tname = ' in option and '\n\t\tname = "' not in option else index + 1
#                        expected_logging_line = 'log = "' + logging_loc + ': event ' + event_id + ' option ' + str(option_name) + '"'
#                        has_valid_logging = expected_logging_line in option
#
#                        if not has_valid_logging:
#                            if has_any_logging and not has_data_logging:
#                                str_to_replace = re.findall('log =.*', option)[0]
#                                dict_with_str_to_replace_option[option] = option.replace(str_to_replace, expected_logging_line)
#                            if has_any_logging and has_data_logging:
#                                if option.count("log =") == 1:
#                                    x = re.findall(r'^\toption = .*', option, flags=re.MULTILINE)[0]
#                                    dict_with_str_to_replace_option[option] = option.replace(x, f'{x}\n\t\t{expected_logging_line}')
#                                else:
#                                    str_to_replace = re.findall(r'log = \"(?!KR_Event_Logging).*', option)[0]
#                                    dict_with_str_to_replace_option[option] = option.replace(str_to_replace, expected_logging_line)
#                            if not has_any_logging:
#                                x = re.findall(r'^\toption = .*', option, flags=re.MULTILINE)[0]
#                                dict_with_str_to_replace_option[option] = option.replace(x, f'{x}\n\t\t{expected_logging_line}')
#
#                        for key, value in dict_with_str_to_replace_option.items():
#                            dict_with_str_to_replace_event[event] = event.replace(key, value) if event not in dict_with_str_to_replace_event.keys() else dict_with_str_to_replace_event[event].replace(key, value)
#
#                for key, value in dict_with_str_to_replace_event.items():
#                    text_file = text_file.replace(key, value)
#                with open(filename, 'w', encoding="utf-8-sig") as text_file_write:
#                    text_file_write.write(text_file)
#
#    for filename in glob.iglob(filepath_to_events + '**/*.txt', recursive=True):
#        if DataCleaner.skip_files(files_to_skip=files_to_skip, filename=filename):
#            continue
#
#        text_file = FileOpener.open_text_file(filename, lowercase=False)
#        pattern_matches = re.findall(r'^country_event = \{(.*?)^\}', text_file, flags=re.DOTALL | re.MULTILINE)
#        if len(pattern_matches) > 0:
#            for event in pattern_matches:
#                event_id = re.findall(r'^\tid = ([^ \n\t]+)', event, flags=re.MULTILINE)[0]
#
#                hidden_event = "donotlog" in event
#                if event_id in false_positives or hidden_event:
#                    continue
#
#                options = re.findall(r'(^\toption = \{.*?^\t\})', event, flags=re.DOTALL | re.MULTILINE)
#
#                for index, option in enumerate(options):
#                    if 'log = "[GetLogInfo]: event ' + event_id not in option:
#                        print(f'{event_id}, option {index} - missing logging')

    # 2. Event logging - immediate
    for event_type, logging_loc in immediate_event_logging_args.items():
        for filename in glob.iglob(filepath_to_events + '**/*.txt', recursive=True):
            if DataCleaner.skip_files(files_to_skip=files_to_skip, filename=filename):
                continue

            text_file = FileOpener.open_text_file(filename, lowercase=False)
            pattern_event = '^' + event_type + r' = \{(.*?)^\}'
            pattern_matches = re.findall(pattern_event, text_file, flags=re.DOTALL | re.MULTILINE)
            if len(pattern_matches) > 0:
                dict_with_str_to_replace = dict()
                for event in pattern_matches:
                    #print(event_id)
                    event_id = re.findall(r'^(?:\t|    )id = ([^ \n\t]+)', event, flags=re.MULTILINE)[0]
                    if event_id in false_positives:
                        continue

                    hidden_event = "hidden = yes" in event or "donotlog" in event
                    has_any_logging = "immediate = { log =" in event or "immediate = {log =" in event
                    expected_logging_line = 'immediate = { log = "[GetDateText]: [Root.GetName]: event ' + event_id + '" }'
                    has_valid_logging = expected_logging_line in event

                    if not has_valid_logging: #and not hidden_event:
                        if has_any_logging:
                            try :
                                str_to_replace = re.findall(r'immediate = *\{ *log =.*', event)[0]
                            except Exception:
                                print(event)
                                raise
                            dict_with_str_to_replace[event] = event.replace(str_to_replace, expected_logging_line)
                        if not has_any_logging:
                            x = re.findall(r'^(?:\t|    )id = .*', event, flags=re.MULTILINE)[0]
                            dict_with_str_to_replace[event] = event.replace(x, f'{x}\n\t{expected_logging_line}')

                for key, value in dict_with_str_to_replace.items():
                    text_file = text_file.replace(key, value)
                with open(filename, 'w', encoding="utf-8-sig") as text_file_write:
                    text_file_write.write(text_file)


def format_logging_decisions(username, mod_name):
    """Add logging to decisions

    Args:
        username (_type_): windows username
        mod_name (_type_): mod folder name
    """
    test_runner = TestRunner(username, mod_name)
    filepath_to_decisions = f'{test_runner.full_path_to_mod}common\\decisions\\'

    for filename in glob.iglob(filepath_to_decisions + '**/*.txt', recursive=True):
        if '\\categories' in filename or "Generic decisions" in filename:
            continue
        text_file = FileOpener.open_text_file(filename, lowercase=False)
        pattern_matches = re.findall('^\\t[^\\t#]+ = \\{.*?^\\t\\}', text_file, flags=re.MULTILINE | re.DOTALL)
        if len(pattern_matches) > 0:
            dict_with_str_to_replace = dict()
            for dec in pattern_matches:
                dec_id = re.findall('^\\t([^\t]+) = \\{', dec, flags=re.MULTILINE)[0]

                donotlog = "donotlog" in dec
                if donotlog:
                    continue

                cancel_effect = re.findall('(\\t+)cancel_effect = \\{([^\\n]*|.*?^\\1)\\}', dec, flags=re.DOTALL | re.MULTILINE)[0][1] if 'cancel_effect =' in dec else False
                complete_effect = re.findall('(\\t+)complete_effect = \\{([^\\n]*|.*?^\\1)\\}', dec, flags=re.DOTALL | re.MULTILINE)[0][1] if 'complete_effect =' in dec else False
                remove_effect = re.findall('(\\t+)remove_effect = \\{([^\\n]*|.*?^\\1)\\}', dec, flags=re.DOTALL | re.MULTILINE)[0][1] if 'remove_effect =' in dec else False
                timeout_effect = re.findall('(\\t+)timeout_effect = \\{([^\\n]*|.*?^\\1)\\}', dec, flags=re.DOTALL | re.MULTILINE)[0][1] if 'timeout_effect =' in dec else False
                is_targeted = "FROM" in dec or "state_target = yes" in dec or "target_trigger" in dec or "target_root_trigger" in dec
                target_line = " target: [From.GetName]" if is_targeted else ""
                expected_logging_line_cancel = 'log = "[GetDateText]: [Root.GetName]: Decision cancel ' + dec_id + target_line + '"'
                expected_logging_line_complete = 'log = "[GetDateText]: [Root.GetName]: Decision complete ' + dec_id + target_line + '"'
                expected_logging_line_remove = 'log = "[GetDateText]: [Root.GetName]: Decision remove ' + dec_id + target_line + '"'
                expected_logging_line_timeout = 'log = "[GetDateText]: [Root.GetName]: Decision timeout ' + dec_id + target_line + '"'
                has_any_logging_cancel = 'cancel_effect = {\n\t\t\tlog' in dec
                has_any_logging_complete = 'complete_effect = {\n\t\t\tlog' in dec
                has_any_logging_remove = 'remove_effect = {\n\t\t\tlog' in dec
                has_any_logging_timeout = 'timeout_effect = {\n\t\t\tlog' in dec
                fixed_decision_code = dec

                if cancel_effect:
                    if expected_logging_line_cancel not in cancel_effect:
                        if has_any_logging_cancel:
                            str_to_replace_cancel = re.findall('cancel_effect = \\{.*\\n\\t+log =.*', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_cancel, 'cancel_effect = {\n\t\t\t' + expected_logging_line_cancel)

                        if not has_any_logging_cancel:
                            str_to_replace_cancel = re.findall('cancel_effect = \\{', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_cancel, 'cancel_effect = {\n\t\t\t' + expected_logging_line_cancel)

                if complete_effect:
                    if expected_logging_line_complete not in complete_effect:
                        if has_any_logging_complete:
                            str_to_replace_complete = re.findall('complete_effect = \\{.*\\n\\t+log =.*', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_complete, 'complete_effect = {\n\t\t\t' + expected_logging_line_complete)

                        if not has_any_logging_complete:
                            str_to_replace_complete = re.findall('complete_effect = \\{', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_complete, 'complete_effect = {\n\t\t\t' + expected_logging_line_complete)

                if remove_effect:
                    if expected_logging_line_remove not in remove_effect:
                        if has_any_logging_remove:
                            str_to_replace_remove = re.findall('remove_effect = \\{.*\\n\\t+log =.*', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_remove, 'remove_effect = {\n\t\t\t' + expected_logging_line_remove)

                        if not has_any_logging_remove:
                            str_to_replace_remove = re.findall('remove_effect = \\{', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_remove, 'remove_effect = {\n\t\t\t' + expected_logging_line_remove)

                if timeout_effect:
                    if expected_logging_line_timeout not in timeout_effect:
                        if has_any_logging_timeout:
                            str_to_replace_timeout = re.findall('timeout_effect = \\{.*\\n\\t+log =.*', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_timeout, 'timeout_effect = {\n\t\t\t' + expected_logging_line_timeout)

                        if not has_any_logging_timeout:
                            str_to_replace_timeout = re.findall('timeout_effect = \\{', dec)[0]
                            fixed_decision_code = fixed_decision_code.replace(str_to_replace_timeout, 'timeout_effect = {\n\t\t\t' + expected_logging_line_timeout)

                if fixed_decision_code != dec:
                    dict_with_str_to_replace[dec] = fixed_decision_code

            for key, value in dict_with_str_to_replace.items():
                text_file = text_file.replace(key, value)
            with open(filename, 'w', encoding="utf-8") as text_file_write:
                text_file_write.write(text_file)


def format_logging_focuses(username, mod_name):
    """Add logging to focuses

    Args:
        username (_type_): windows username
        mod_name (_type_): mod folder name
    """
    test_runner = TestRunner(username, mod_name)
    filepath_to_focuses = f"{test_runner.full_path_to_mod}common\\national_focus\\"

    # Regular focus
    for filename in glob.iglob(filepath_to_focuses + '**/*.txt', recursive=True):
        text_file = FileOpener.open_text_file(filename, lowercase=False)
        pattern_matches = re.findall(r'^\s*focus = \{.*?^\s*\}', text_file, flags=re.MULTILINE | re.DOTALL)
        if len(pattern_matches) > 0:
            dict_with_str_to_replace = dict()
            for focus in pattern_matches:
                focus_id = re.findall(r'^\s*id = ([^\s]+)', focus, flags=re.MULTILINE)[0]

                select_effect_match = re.findall(r'(\t+)select_effect = \{([^\n]*|.*?^\1)\}', focus, flags=re.DOTALL | re.MULTILINE)
                select_effect = select_effect_match[0][1] if select_effect_match else False
                complete_effect_match = re.findall(r'(\t+)completion_reward = \{([^\n]*|.*?^\1)\}', focus, flags=re.DOTALL | re.MULTILINE)
                complete_effect = complete_effect_match[0][1] if complete_effect_match else False

                expected_logging_line_select = 'log = "[GetDateText]: [Root.GetName]: Select Focus ' + focus_id + '"'
                expected_logging_line_complete = 'log = "[GetDateText]: [Root.GetName]: Focus ' + focus_id + '"'

                has_any_logging_select = 'select_effect = {\n\t\t\tlog' in focus
                has_any_logging_complete = 'completion_reward = {\n\t\t\tlog' in focus

                fixed_focus_code = focus

                if select_effect:
                    if expected_logging_line_select not in select_effect:
                        if has_any_logging_select:
                            str_to_replace_select = re.findall(r'select_effect = \{.*\n\t+log =.*', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_select, 'select_effect = {\n\t\t\t' + expected_logging_line_select)

                        if not has_any_logging_select:
                            str_to_replace_select = re.findall(r'select_effect = \{', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_select, 'select_effect = {\n\t\t\t' + expected_logging_line_select)

                if complete_effect:
                    if expected_logging_line_complete not in complete_effect:
                        if has_any_logging_complete:
                            str_to_replace_complete = re.findall(r'completion_reward = \{.*\n\t+log =.*', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_complete, 'completion_reward = {\n\t\t\t' + expected_logging_line_complete)

                        if not has_any_logging_complete:
                            str_to_replace_complete = re.findall(r'completion_reward = \{', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_complete, 'completion_reward = {\n\t\t\t' + expected_logging_line_complete)

                if fixed_focus_code != focus:
                    dict_with_str_to_replace[focus] = fixed_focus_code

            for key, value in dict_with_str_to_replace.items():
                text_file = text_file.replace(key, value)
            with open(filename, 'w', encoding="utf-8") as text_file_write:
                text_file_write.write(text_file)

    # Shared focus
    for filename in glob.iglob(filepath_to_focuses + '**/*.txt', recursive=True):
        text_file = FileOpener.open_text_file(filename, lowercase=False)
        pattern_matches = re.findall(r'^shared_focus = \{.*?^\}', text_file, flags=re.MULTILINE | re.DOTALL)
        if len(pattern_matches) > 0:
            dict_with_str_to_replace = dict()
            for focus in pattern_matches:
                focus_id = re.findall(r'^\s*id = ([^\s]+)', focus, flags=re.MULTILINE)[0]

                select_effect_match = re.findall(r'(\t+)select_effect = \{([^\n]*|.*?^\1)\}', focus, flags=re.DOTALL | re.MULTILINE)
                select_effect = select_effect_match[0][1] if select_effect_match else False
                complete_effect_match = re.findall(r'(\t+)completion_reward = \{([^\n]*|.*?^\1)\}', focus, flags=re.DOTALL | re.MULTILINE)
                complete_effect = complete_effect_match[0][1] if complete_effect_match else False

                expected_logging_line_select = 'log = "[GetDateText]: [Root.GetName]: Select Focus ' + focus_id + '"'
                expected_logging_line_complete = 'log = "[GetDateText]: [Root.GetName]: Focus ' + focus_id + '"'

                has_any_logging_select = 'select_effect = {\n\t\tlog' in focus
                has_any_logging_complete = 'completion_reward = {\n\t\tlog' in focus

                fixed_focus_code = focus

                if select_effect:
                    if expected_logging_line_select not in select_effect:
                        if has_any_logging_select:
                            str_to_replace_select = re.findall(r'select_effect = \{.*\n\t+log =.*', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_select, 'select_effect = {\n\t\t' + expected_logging_line_select)

                        if not has_any_logging_select:
                            str_to_replace_select = re.findall(r'select_effect = \{', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_select, 'select_effect = {\n\t\t' + expected_logging_line_select)

                if complete_effect:
                    if expected_logging_line_complete not in complete_effect:
                        if has_any_logging_complete:
                            str_to_replace_complete = re.findall(r'completion_reward = \{.*\n\t+log =.*', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_complete, 'completion_reward = {\n\t\t' + expected_logging_line_complete)

                        if not has_any_logging_complete:
                            str_to_replace_complete = re.findall(r'completion_reward = \{', focus)[0]
                            fixed_focus_code = fixed_focus_code.replace(str_to_replace_complete, 'completion_reward = {\n\t\t' + expected_logging_line_complete)

                if fixed_focus_code != focus:
                    dict_with_str_to_replace[focus] = fixed_focus_code

            for key, value in dict_with_str_to_replace.items():
                text_file = text_file.replace(key, value)
            with open(filename, 'w', encoding="utf-8") as text_file_write:
                text_file_write.write(text_file)


if __name__ == '__main__':
    format_logging_events(username=os.getlogin(), mod_name="equestria_dev")
    #format_logging_decisions(username=os.getlogin(), mod_name="equestria_dev")
    #format_logging_focuses(username=os.getlogin(), mod_name="equestria_dev")