import codecs
import os
import re
import sys
from pathlib import Path

source_dir = Path('./countries/')


for filename in source_dir.glob('*.txt'):
    fstr = ""
    with codecs.open(filename, mode='r', encoding='utf-8-sig') as f:
        fstr = f.read()
    groups = re.search(r"set_popularities = {\n\s*(?:democratic|fascism|communism|neutrality)\s*=\s*([0-9]+)\n\s*(?:democratic|fascism|communism|neutrality)\s*=\s*([0-9]+)\n\s*(?:democratic|fascism|communism|neutrality)\s*=\s*([0-9]+)\n\s*(?:democratic|fascism|communism|neutrality)\s*=\s*([0-9]+)", fstr)
    if groups:
        nums = int(groups.group(1)) + int(groups.group(2)) + int(groups.group(3)) + int(groups.group(4))
        if nums != 100:
            print("%s has wrong popularities" % filename)
