import urllib.request
import os
import glob
import pathlib
import re
import string

RE_COMMENT = re.compile(r'^(.*?)#([^"]*)$')
RE_ENTRY = re.compile(r'\s*(\w+):\d*\s+"(.*)"$')
RE_FILTER = re.compile(r"((?<!\\)\[.+\])|((?<!\\)\$\w+\$)|((?<!\\)£\w+)|((?<!\\)§.*?§!)|(\\\w)")
RE_PUNCTUATION = re.compile(('[%s]' % re.escape(string.punctuation + "—")))

LOC_FILE_EXTENSION = ".yml"

EN_WORD_LIST = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt"

def get_english_words_set(filename, targeturl, override=False):
    out_set = set()
    if os.path.exists(filename) and not override:
        with open(filename, "r") as fd:
            line = fd.readline().strip().lower()
            while line:
                out_set.add(line)
                line = fd.readline().strip().lower()
        return out_set

    with open(filename, "w") as fd, urllib.request.urlopen(targeturl) as url:
        for line in url:
            word = line.decode("utf-8").strip().lower()
            fd.write(word)
            fd.write('\n')
            out_set.add(word)
    return out_set

def get_loc_keys(filename):
    out_dict = {}
    with open(filename, "r", encoding="utf-8") as fd:
        line = fd.readline()
        line_number = 0
        while line:
            line_number += 1
            # Ignore the comments
            match = RE_COMMENT.match(line)
            if match:
                line = match.group(1)

            # See if it is an entry
            match = RE_ENTRY.match(line.strip())
            if not match:
                line = fd.readline()
                continue
            entry_name, entry_content = match.group(1), match.group(2)

            # Filter content (Delete code related part)
            entry_content = RE_FILTER.sub(" ", entry_content)

            out_dict[entry_name] = (line_number, entry_content)
            line = fd.readline()
    return out_dict

def get_loc_file_list(target):
    list_file = []
    if not os.path.exists(target):
        return list_file
    if os.path.isdir(target):
        for file in glob.glob(os.path.join(target ,'**', '*'), recursive=True):
            path = pathlib.Path(file)
            if path.suffix == LOC_FILE_EXTENSION:
                list_file.append(file)
    else:
        list_file = [target]
    return list_file

def split_words_error(entry, word_list):
    out_word = []
    # Split the entry
    words = RE_PUNCTUATION.sub(" ", entry).split(" ")
    for word in words:
        if word and word.lower() not in word_list:
            out_word.append(word)
    return out_word

file_list = get_loc_file_list("../../localisation/english")
word_list = get_english_words_set("en_word.txt", EN_WORD_LIST)
word_error_dict = [{}, {}] # One side capitalized, the other not. Key: word, content dict with as key the entry and value the number of error in the entry
for file in file_list:
    loc_keys = get_loc_keys(file)
    for entry, data in loc_keys.items():
        list_error = split_words_error(data[1], word_list)
        for error in list_error:
            # Choose in which error dict to put the error
            target = word_error_dict[0 if error[0].isupper() else 1]

            # Add the an occurence of error
            if error not in target:
                target[error] = {entry: 1}
            elif entry in target[error]:
                target[error][entry] += 1
            else:
                target[error][entry] = 1

print(list(word_error_dict[1]))
print(len(list(word_error_dict[1])))
exit()

set_word = get_english_words_set("en_word.txt", EN_WORD_LIST, override=True)

out_set = set_word.union(set_word_2)

print(len(set_word))
print(len(out_set))
