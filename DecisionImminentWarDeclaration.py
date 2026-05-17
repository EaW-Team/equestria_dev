from codecs import open
import sys
from os import listdir
import time
import os
import re

complete_effect = "eaw_alert_send_imminent_declaration_of_war"
complete_effect_var = "temp_target"
remove_effect = "eaw_clear_alert_imminent_declaration_of_war"
remove_effect_var = "temp_target"
complete_effect_targeted = "eaw_alert_send_imminent_declaration_of_war_FROM"
remove_effect_targeted = "eaw_clear_alert_imminent_declaration_of_war_FROM"

def decision_improved(cpath):

    timestart = time.time()

    # Thanks Yard Very Cool
    for filename in listdir(os.path.join(cpath, "common", "decisions")):

        # listdir also provides directories and this is very annoying thank you very much
        if 'categories' in filename:
            continue

        # We gottem boys
        # This check is here because sometimes smart people put other files in this directory
        if ".txt" in filename:
            # Open that sucker right up
            with open(os.path.join(cpath, "common", "decisions", filename), 'r', 'utf-8') as file:

                # Because this scripts hates empty files, we just ignore all that are below 100 bytes
                if os.path.getsize(os.path.join(cpath, "common", "decisions", filename)) < 100:
                    continue

                # Get them lines
                lines = file.readlines()

                # This is the var that indicates the bracket level
                level = 0

                # The dictionary that will hold all our stuff
                found_decisions = {}  # Numbers denote line numbers: decision_name: [complete_effect, remove_effect, timeout_effect, targeted_decision_bool]

                #Initialise the latest found to an unreachable value
                latest_found = -1

                # Loop over all lines this file to detect where the decisions are
                for line_number, line in enumerate(lines):

                    # If the line is a comment, we skip it, and if it contains a comment, strip it out
                    if '#' in line:
                        if line.strip().startswith("#") is True:
                            continue
                        else:
                            line = line.split('#')[0]

                    # Check for a ={ and the right level denoting a new decision
                    if ('= {' in line or '={' in line) and level == 1:

                        # Keep track of the latest decision found
                        latest_found = line_number
                        # Add a default reference to this decision
                        #[complete_effect line, remove_effect/timeout_effect line, war target lines, is targeted, has complete_effect, has effects, should change]
                        found_decisions[line_number] = [0, 0, [], False, False, False, False]

                    if latest_found in found_decisions:
                        if 'complete_effect' in line:
                            found_decisions[latest_found][0] = line_number
                            found_decisions[latest_found][4] = True

                        elif 'remove_effect' in line or 'timeout_effect' in line:
                            found_decisions[latest_found][1] = line_number

                        elif 'war_with_on_remove' in line or 'war_with_target_on_remove' in line or 'war_with_target_on_timeout' in line or 'war_with_on_timeout' in line:
                            target = line.split('=')[1].strip()
                            if target != "yes":
                                found_decisions[latest_found][2].append(target)
                            found_decisions[latest_found][6] = True

                        elif 'target_trigger' in line or 'targets' in line or 'target_array' in line:
                            found_decisions[latest_found][3] = True

                        #Ignore the decision if it already has the scripted effects
                        elif complete_effect in line or complete_effect_targeted in line or remove_effect in line or remove_effect_targeted in line:
                            found_decisions[latest_found][5] = True

                    #If the decision has no complete_effect we'll insert it right before the decision ends
                    if ('}' in line) and level == 2:
                        if found_decisions[latest_found][0] == 0:
                            found_decisions[latest_found][0] = line_number-1

                    if '{' in line:
                        level += line.count('{')
                    if '}' in line:
                        level -= line.count('}')


            if found_decisions == {}:
                continue

            found_decisions_filtered = {}
            for key, value in found_decisions.items():
                # Check if key is even then add pair to new dictionary
                if value:
                    found_decisions_filtered[key] = value

            found_decisions = found_decisions_filtered

            id = ""
            index = [-1, -1, [], False, False, False, False]

            main_line_numbers = list(found_decisions.keys())

            skip_next = False

            with open(os.path.join(cpath, "common", "decisions", filename), 'w', 'utf-8') as outputfile:
                outputfile.truncate()

                for line_number, line in enumerate(lines):

                    if skip_next:
                        skip_next = False
                        continue

                    if line.strip().startswith('#'):
                        outputfile.write(line)
                        continue

                    replacement_text = line

                    #For neatness we want to insert the code under any logs

                    if (line_number in main_line_numbers) and not found_decisions[line_number][5] and found_decisions[line_number][6]:
                        index = found_decisions[line_number]

                    #Add to complete_effect
                    elif line_number == index[0]:
                        if line_number < (len(lines) - 1) and "log" in lines[line_number + 1]:
                            replacement_text = replacement_text + lines[line_number + 1]
                            skip_next = True
                        insertion_text = ""
                        if index[3]:
                            insertion_text = complete_effect_targeted + " = yes"
                        else:
                            for tag in index[2]:
                                insertion_text += "set_temp_variable = { " + complete_effect_var + " = " + tag + " }\n\t\t\t" + complete_effect + " = yes\n\t\t\t"
                        if not index[4]:
                            insertion_text = "\n\t\tcomplete_effect = {\n\t\t\t" + insertion_text + "\n\t\t}\n"
                            replacement_text = replacement_text + insertion_text
                        else:
                            if '}' in line:
                                replacement_text = replacement_text.split('}')[0] + "\t\t\t" + insertion_text + "\n\t\t}\n"
                            else:
                                replacement_text = replacement_text + "\t\t\t" + insertion_text + "\n"

                    #Add to remove_effect or timeout_effect
                    elif line_number == index[1]:
                        if line_number < (len(lines) - 1) and "log" in lines[line_number + 1]:
                            replacement_text = replacement_text + lines[line_number + 1]
                            skip_next = True
                        insertion_text = ""
                        if index[3]:
                            insertion_text = remove_effect_targeted + " = yes"
                        else:
                            for tag in index[2]:
                                insertion_text += "set_temp_variable = { " + remove_effect_var + " = " + tag + " }\n\t\t\t" + remove_effect + " = yes\n\t\t\t"
                        if '}' in line:
                            replacement_text = replacement_text.split('}')[0] + "\t\t\t" + insertion_text + "\n\t\t}\n"
                        # # # else:
                            replacement_text = replacement_text + "\t\t\t" + insertion_text + "\n"

                    outputfile.write(replacement_text)

    return time.time() - timestart


def main():
    cpath = os.path.dirname(os.path.realpath(__file__))

    ttime = 0
    ttime += decision_improved(cpath)
    print("Total Time: %.3f ms" % (ttime * 1000))

if __name__ == "__main__":
    main()