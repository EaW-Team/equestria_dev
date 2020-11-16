#!/usr/bin/python
import argparse
import os
import sys
import re

#############################
###
### HoI 4 idea GFX entry generator by Yard1, originally for Equestria at War mod
### Written in Python 2.7
###
### Copyright (c) 2017 Antoni Baum (Yard1)
### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
### usage: hoi4ideagfxentry.py [-h] [--icon_directory icon_directory]
###                               [--icon_format icon_format]
###                               idea_file gfx_file
###
### Given a folder and an idea file, add GFX entries to a specified file or create
### a new .gfx file if none exists.
### 
### positional arguments:
###   idea_file             Name of the idea file
###   gfx_file              Name of the gfx file to add to (will create a new .gfx
###                         file if none exists)
### 
### optional arguments:
###   -h, --help            show this help message and exit
###   --icon_directory icon_directory
###                         Directory in gfx/interface/ideas where idea icons are
###                         located (default:"")
###   --icon_format icon_format
###                         Format of icon files, without dot (default: dds)
###   -np, --no_prefix      Do not add idea_ prefix to icon file names (Default:
###                         True)
###
#############################
def readfile(name):
    print("Reading file " + name + "...")
    with open(name, "r") as f:
        lines = f.read().splitlines()
    pictures = list()

    open_blocks = 0
    picture = ""
    for line in lines:
        line = re.sub('#.*', "", line)
        if open_blocks < 3 and picture != "":
            if picture not in pictures:
                pictures.append(picture)
            picture = ""
        if open_blocks == 2 and "{" in line:
            temp_line = line
            temp_line = re.sub('\s|=(\s|){', "", temp_line)
            temp_line.strip()
            picture = temp_line
        if open_blocks > 2 and ("picture =" in line or "picture=" in line):
            temp_line = line
            temp_line = re.sub('(\s|).*=(\s|)', "", temp_line)
            temp_line.strip()
            picture = temp_line
        open_blocks += line.count('{')
        open_blocks -= line.count('}')

    print("File %s read successfully, %s unique idea pictures found." % (name, str(len(pictures))))
    return pictures

def find_index_before_bracket(lines):
    after_bracket = False
    index_to_insert = 0
    for i, line in reversed(list(enumerate(lines))):
        if "}" in line:
            after_bracket = True
            index_to_insert = i
            break
    return index_to_insert
#############################
parser = argparse.ArgumentParser(description='Given a folder and an idea file, add GFX entries to a specified file or create a new .gfx file if none exists.')
parser.add_argument('idea_file', metavar='idea_file',
                    help='Name of the idea file')
parser.add_argument('gfx_file', metavar='gfx_file',
                    help='Name of the gfx file to add to (will create a new .gfx file if none exists)')
parser.add_argument('--icon_directory', metavar='icon_directory', default="", required=False,
                    help='Directory in gfx/interface/ideas where idea icons are located (default:\"\")')
parser.add_argument('--icon_format', metavar='icon_format', default="dds", required=False,
                    help='Format of icon files, without dot (default: dds)')
parser.add_argument( '-np', '--no_prefix', action='store_true', required=False,
                    help='Do not add idea_ prefix to icon file names (Default: True)')

args = parser.parse_args()
prefix = ""
if args.no_prefix:
    prefix = "idea_"
parsed_file = readfile(args.idea_file)
added_pictures = 0
lines = list()

if os.path.exists(args.gfx_file):
    with open(args.gfx_file, "r") as f:
        lines = f.read().splitlines()
if len(lines) < 1:
    lines = ["spriteTypes = {", "}"]

if args.icon_directory != "":
    args.icon_directory = "/" + args.icon_directory

for idea in parsed_file:
    index_to_insert = find_index_before_bracket(lines)

    gfx_entry_name = "GFX_idea_%s" % idea

    if any(re.search(("name(\s|).*=(\s|).*\"%s\"" % gfx_entry_name), line) for line in lines):
        continue

    lines.insert(index_to_insert, "\t}")
    lines.insert(index_to_insert, "\t\ttexturefile = \"gfx/interface/ideas%s/%s.%s\"" % (args.icon_directory, ("%s%s" % (prefix, idea)), args.icon_format))
    lines.insert(index_to_insert, "\t\tname = \"%s\"" % gfx_entry_name)
    lines.insert(index_to_insert, "\tSpriteType = {")
    added_pictures = added_pictures + 1

with open(args.gfx_file,"w+") as f:
    f.writelines(str(line) + "\n" for line in lines)
print("GFX file %s written to successfully, added %s new GFX entries" % (args.gfx_file, str(added_pictures)))
