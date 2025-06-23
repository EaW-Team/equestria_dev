# -*- coding: utf-8 -*-

import urllib.request
from urllib.error import URLError
import os
import glob
import pathlib
import re
import string
import argparse
import json

from config import *

def parse_argument():
    """Command line options management"""
    parser = argparse.ArgumentParser(description="A flexible spell checker for Paradox localisation")
    parser.add_argument("-d", "--dictionnary", help="Dictionnary directory path. Contains a list of valid words")
    parser.add_argument("-e", "--exception", help="Exception directory path. Contain a list of exceptions")
    parser.add_argument("-l", "--language", default="en", help="Language selection. Will ensure to download up to date word list(s) into the dictionnary folder")
    parser.add_argument("-r", "--report", help="Log file location. If define, copy the console output to this file")
    parser.add_argument("-te", "--target-extension", default=LOC_FILE_EXTENSION, help="File extension that is considered localisation")
    parser.add_argument("--json-wordlist", default=DEFAULT_WORDLIST_JSON, help="Path to a json file containing a word list for different languages")
    parser.add_argument("--no-wordlist-update", action="store_true", help="Do not download the wordlist linked in the JSON wordlist. Useful in case of offline work")
    parser.add_argument("target", help="Path to either a file or directory to parse recursivly for localisation")

    return parser.parse_args()

def list_files(target, extension=None):
    """List file in a directory recursivly."""
    list_file = []
    if not os.path.exists(target):
        return list_file
    if os.path.isdir(target):
        for file in glob.glob(os.path.join(target ,'**', '*'), recursive=True):
            path = pathlib.Path(file)
            if extension and path.suffix == extension:
                list_file.append(file)
    else:
        list_file = [target]
    return list_file

def download_wordlist(filename, url):
    """Download the text file stored in the URL into a file"""
    try:
        with open(filename, "w") as fd, urllib.request.urlopen(url) as url:
            for line in url:
                word = line.decode("utf-8").strip().lower()
                fd.write(word)
                fd.write('\n')
    except URLError:
        print(f"Cannot acces {url}.\n\
Check your internet connection, the availability of the ressources \
or run with the option --no-wordlist-update if the file has already been downloaded")
        exit()

def parse_dict_file(filename, out_set):
    """Open a dictionnary file and add all the words into a set"""
    with open(filename, "r") as fd:
        line = fd.readline().strip().lower()
        while line:
            out_set.add(line)
            line = fd.readline().strip().lower()

if __name__ == "__main__":
    args = parse_argument()

    dict_folder = args.dictionnary
    if dict_folder == None:
        dict_folder = DEFAULT_DICTIONNARY_FORMAT.format(args.language)

    # Create the folder if it doesn't exist
    os.makedirs(dict_folder, exist_ok=True)


    with open(args.json_wordlist, "r") as fd:
        wordlist = json.load(fd)

    if args.language not in wordlist:
        print(f"The languague {args.language} is not defined in the file {args.json_wordlist}")
        print("No wordlist will be downloaded")

    elif not args.no_wordlist_update:
        print(f"Updating the word list for {args.language}")
        for filename, link in wordlist[args.language].items():
            download_wordlist(os.path.join(dict_folder, filename + DICT_EXTENSION), link)

    # Parse the dictionnary folder for txt files
    dict_words = set()
    dict_files = list_files(dict_folder, extension=DICT_EXTENSION)
    for file in dict_files:
        parse_dict_file(file, dict_words)

    print(f"The library contains {len(dict_words)} different words")




exit()

# Draft

RE_COMMENT = re.compile(r'^(.*?)#([^"]*)$')
RE_ENTRY = re.compile(r'\s*(\w+):\d*\s+"(.*)"$')
RE_FILTER = re.compile(r"((?<!\\)\[.+\])|((?<!\\)\$\w+\$)|((?<!\\)£\w+)|((?<!\\)§.*?§!)|(\\\w)")
RE_PUNCTUATION = re.compile(('[%s]' % re.escape(string.punctuation + "—")))


EN_WORD_LIST_LINK = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words.txt"

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

def split_words_error(entry, word_list):
    out_word = []
    # Split the entry
    words = RE_PUNCTUATION.sub(" ", entry).split(" ")
    for word in words:
        if word and word.lower() not in word_list:
            out_word.append(word)
    return out_word

file_list = list_files("../../localisation/english", LOC_FILE_EXTENSION)
file_list = list_files(".", ".txt")
print(file_list)
exit()

word_list = get_english_words_set(os.path.join(target , "en_word.txt"), EN_WORD_LIST_LINK)
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
