#!/usr/bin/python3
import argparse
import os
import re
import glob
import sys

#############################
###
### HoI 4 Province ID Recycler by Yard1, originally for Equestria at War mod
### Written in Python 3.6
###
### Copyright (c) 2017 Antoni Baum (Yard1)
### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
### usage: hoi4provinceidrecycler.py [-h] definition ids [ids ...]
###
### Recycle given province IDs in the given definition.csv file.
###
### positional arguments:
###   definition  Path to definition.csv file
###   ids         Province IDs to find - space separated list
###
### optional arguments:
###   -h, --help  show this help message and exit
###
#############################

def read_file(name, ids):
    print("Reading file " + name + "...")
    with open(name, "r") as f:
        lines = f.read().splitlines()
    
    for id in ids:
        found_idx = -1
        for idx, line in enumerate(lines):
            if line.startswith(str(id) + ";"):
                found_idx = idx
                break

        if found_idx < 0:
            print("ID %s not found!" % str(id))
            continue
        print("Found ID %s at line %s" % (str(id), str(found_idx)))

        split_last_line = lines.pop().split(";", 1)
        split_found_line = lines[found_idx].split(";", 1)
        split_found_line[1] = split_last_line[1]
        lines[found_idx] = ';'.join(split_found_line)

    print("Writing to file " + name + "...")
    with open(name, "w") as f:
        f.writelines(str(line) + "\n" for line in lines)

#############################
parser = argparse.ArgumentParser(description='Recycle given province IDs in the given definition.csv file.')
parser.add_argument('definition', metavar='definition',
                    help='Path to definition.csv file')
parser.add_argument('ids', nargs='+', type=int,
                    help='Province IDs to find - space separated list')
                    
args = parser.parse_args()

read_file(args.definition, args.ids)
