#!/usr/bin/python
import argparse
import os
import sys
import glob
import re
import datetime

#############################
###
### HoI 4 Focus GFX entry generator by Yard1, originally for Equestria at War mod
### TURNED INTO IDEA GFX ENTRY BY SCROUP ))))
### Written in Python 2.7
###
### Copyright (c) 2017 Antoni Baum (Yard1)
### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
### usage: hoi4FocusGFXEntryApp.py [-h] [-d--directory directory] [--goals goals]
###                                [--goals_shine goals_shine]
###                                idea_name
### 
### Given a folder and a focus name, look for specified .gfx files and add GFX
### entries for the focus name.
### 
### positional arguments:
###   idea_name            Name of the focus icon GFX entry (without GFX_ at the
###                         beginning)
### 
### optional arguments:
###   -h, --help            show this help message and exit
###   -d--directory directory
###                         Directory to look for .gfx files in (default: working
###                         directory)
###   --goals goals         Name of the goals file (default:"goals.gfx")
###   --goals_shine goals_shine
###                         Name of the goals_shine file
###                         (default:"goals_shine.gfx")
###
###
#############################
def readable_dir(prospective_dir):
  if not os.path.isdir(prospective_dir):
    raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
  if os.access(prospective_dir, os.R_OK):
    return prospective_dir
  else:
    raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

def find_index_before_bracket(lines):
    after_bracket = False
    index_to_insert = 0
    for i, line in reversed(list(enumerate(lines))):
        if "}" in line:
            after_bracket = True
            index_to_insert = i
            break
    return index_to_insert

parser = argparse.ArgumentParser(description='Given a folder and a focus name, look for specified .gfx files and add GFX entries for the focus name.')
parser.add_argument('idea_name', metavar='idea_name',
                    help='Name of the idea icon GFX entry (without GFX_ at the beginning)')
parser.add_argument('-d' '--directory', metavar='directory', type=str, dest='directory', default=os.getcwd(), required=False,
                    help='Directory to look for .gfx files in (default: working directory)')
parser.add_argument('--ideas', metavar='ideas', default="eaw_ideas.gfx", required=False,
                    help='Name of the ideas file (default:\"eaw_ideas.gfx\")')

args = parser.parse_args()

try:
    dir = readable_dir(args.directory)
except:
   sys.exit("Not a directory! Exiting...")

with open(dir + "/" + args.ideas, "r") as f:
    lines = f.read().splitlines()

index_to_insert = find_index_before_bracket(lines)

lines.insert(index_to_insert, "\t}")
lines.insert(index_to_insert, "\t\ttexturefile = \"gfx/interface/ideas/" + args.idea_name + ".dds\"")
lines.insert(index_to_insert, "\t\tname = \"GFX_idea_" + args.idea_name + "\"")
lines.insert(index_to_insert, "\tSpriteType = {")

with open(dir + "/" + args.ideas,"w+") as f:
    f.writelines(str(line) + "\n" for line in lines)


