# Contains some constants and default configuration for the program
import re

LOC_FILE_EXTENSION = ".yml"
DEFAULT_DICTIONNARY_FORMAT = "dict_{}"
DICT_EXTENSION = ".txt"
DEFAULT_WORDLIST_JSON = "word_list.json"

# Regex for what is the entry in a loc file
RE_LOC_FILE_ENTRY = re.compile(r'\s*(\w+):\d*\s+"(.*)"$')