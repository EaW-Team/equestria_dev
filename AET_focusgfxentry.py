#!/usr/bin/python
import argparse
import os
import sys

#############################
###
### HoI 4 Focus GFX entry generator by Yard1, originally for Equestria at War mod
### Written in Python 2.7
###
### Copyright (c) 2017 Antoni Baum (Yard1)
### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
### usage: hoi4focusgfxentry.py [-h] [-d--directory directory] [--goals goals]
###                                [--goals_shine goals_shine]
###                                icon_name
### 
### Given a folder and a focus name, look for specified .gfx files and add GFX
### entries for the focus name.
### 
### positional arguments:
###   icon_name            Name of the focus icon GFX entry (without GFX_ at the
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
parser.add_argument('icon_name', metavar='icon_name',
                    help='Name of the focus icon GFX entry (without GFX_ at the beginning)')
parser.add_argument('-d' '--directory', metavar='directory', type=str, dest='directory', default=os.getcwd(), required=False,
                    help='Directory to look for .gfx files in (default: working directory)')
parser.add_argument('--goals', metavar='goals', default="focus_AET.gfx", required=False,
                    help='Name of the goals file (default:\"focus_AET.gfx\")')
parser.add_argument('--goals_shine', metavar='goals_shine', default="shine\focus_AET_shine.gfx", required=False,
                    help='Name of the goals_shine file (default:\shine\"focus_AET_shine.gfx\")')

args = parser.parse_args()

try:
    dir = readable_dir(args.directory)
except:
   sys.exit("Not a directory! Exiting...")

with open(dir + "/" + args.goals, "r") as f:
    lines = f.read().splitlines()

index_to_insert = find_index_before_bracket(lines)

lines.insert(index_to_insert, "\t}")
lines.insert(index_to_insert, "\t\ttexturefile = \"gfx/interface/goals/AET/" + args.icon_name + ".tga\"")
lines.insert(index_to_insert, "\t\tname = \"GFX_" + args.icon_name + "\"")
lines.insert(index_to_insert, "\tSpriteType = {")

with open(dir + "/" + args.goals,"w+") as f:
    f.writelines(str(line) + "\n" for line in lines)

with open(dir + "/" + args.goals_shine, "r") as f:
    lines = f.read().splitlines()

index_to_insert = find_index_before_bracket(lines)

lines.insert(index_to_insert, "\t}")
lines.insert(index_to_insert, "\t\tlegacy_lazy_load = no")
lines.insert(index_to_insert, "\t\t}")
lines.insert(index_to_insert, "\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 } ")
lines.insert(index_to_insert, "\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
lines.insert(index_to_insert, "\t\t\tanimationtype = \"scrolling\"      #scrolling, rotating, pulsing")
lines.insert(index_to_insert, "\t\t\tanimationblendmode = \"add\"       #add, multiply, overlay")
lines.insert(index_to_insert, "\t\t\tanimationdelay = 0\t\t\t# in seconds")
lines.insert(index_to_insert, "\t\t\tanimationtime = 0.75\t\t\t\t# in seconds")
lines.insert(index_to_insert, "\t\t\tanimationlooping = no\t\t\t# yes or no ;)")
lines.insert(index_to_insert, "\t\t\tanimationrotation = 90.0\t\t# -90 clockwise 90 counterclockwise(by default)")
lines.insert(index_to_insert, "\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\" \t# <- the animated file")
lines.insert(index_to_insert, "\t\t\tanimationmaskfile = \"gfx/interface/goals/AET/" + args.icon_name + ".tga\"")
lines.insert(index_to_insert, "\t\tanimation = {")
lines.insert(index_to_insert, "\n")
lines.insert(index_to_insert, "\t\t}")
lines.insert(index_to_insert, "\t\t\tanimationtexturescale = { x = 1.0 y = 1.0 } ")
lines.insert(index_to_insert, "\t\t\tanimationrotationoffset = { x = 0.0 y = 0.0 }")
lines.insert(index_to_insert, "\t\t\tanimationtype = \"scrolling\"      #scrolling, rotating, pulsing")
lines.insert(index_to_insert, "\t\t\tanimationblendmode = \"add\"       #add, multiply, overlay")
lines.insert(index_to_insert, "\t\t\tanimationdelay = 0\t\t\t# in seconds")
lines.insert(index_to_insert, "\t\t\tanimationtime = 0.75\t\t\t\t# in seconds")
lines.insert(index_to_insert, "\t\t\tanimationlooping = no\t\t\t# yes or no ;)")
lines.insert(index_to_insert, "\t\t\tanimationrotation = -90.0\t\t# -90 clockwise 90 counterclockwise(by default)")
lines.insert(index_to_insert, "\t\t\tanimationtexturefile = \"gfx/interface/goals/shine_overlay.dds\" \t# <- the animated file")
lines.insert(index_to_insert, "\t\t\tanimationmaskfile = \"gfx/interface/goals/AET/" + args.icon_name + ".tga\"")
lines.insert(index_to_insert, "\t\tanimation = {")
lines.insert(index_to_insert, "\t\t\t\teffectFile = \"gfx/FX/buttonstate.lua\"")
lines.insert(index_to_insert, "\t\ttexturefile = \"gfx/interface/goals/AET/" + args.icon_name + ".tga\"")
lines.insert(index_to_insert, "\t\tname = \"GFX_" + args.icon_name + "_shine\"")
lines.insert(index_to_insert, "\tSpriteType = {")

with open(dir + "/" + args.goals_shine,"w+") as f:
    f.writelines(str(line) + "\n" for line in lines)

