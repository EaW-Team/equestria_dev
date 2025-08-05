#!/usr/bin/python
import argparse
import os
import sys
import glob
import re
import datetime

#############################
###
### HoI 4 Transfer Technology scripted effect generator by Yard1, originally for Equestria at War mod
### Written in Python 2.7
### Transfer Technology scripted effect will grant all techs researched by PREV to ROOT
### Best used when ROOT is just spawned (eg. as a civil war TAG)
### It is not advised to use this for already existing nations, as mutually exclusive techs will be given regardless of what ROOT has already researched
###
### Copyright (c) 2017 Antoni Baum (Yard1)
### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
###
### usage: transfertechgen.py [-h] [-en effectname] [-a | -o] input output
###
### Given an input technology file or folder, generate a Transfer Technology
### scripted effect.
###
### positional arguments:
###   input                 Technology file name/folder containing files
###   output                File name to write the scripted effect to
###
### optional arguments:
###   -h, --help            show this help message and exit
###   -en effectname, --effectname effectname
###                         Name of the scripted effect
###                         (default:"transfer_technology")
###                         (papaerclip default:"paperclip_tech")
###   -a, --add             Will add new technologies to an already existing
###                         transfer_technology effect (first set name with -en)
###   -o, --overwrite       Will overwrite the output file if it already exists
###   -p, --paperclip       Will format the tech for the paperclip_tech scritped effect
###
#############################

def readable_dir(prospective_dir):
  if not os.path.isdir(prospective_dir):
    raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
  if os.access(prospective_dir, os.R_OK):
    return prospective_dir
  else:
    raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

#############################

def readfile(name):
    print("Reading file " + name + "...")
    with open(name, "r") as f:
        lines = f.read().splitlines()
    names = list()

    open_blocks = 0
    is_tech_file = False
    for line in lines:
        line = re.sub('#.*', "", line)
        if "technologies = {" in line:
            is_tech_file = True
        if open_blocks == 1 and "{" in line:
            temp_line = line
            temp_line = re.sub('\s|=(\s|){', "", temp_line)
            names.append(temp_line)
        open_blocks += line.count('{')
        open_blocks -= line.count('}')
    if is_tech_file:
        print("File " + name + " read successfully!")
        return names
    else:
        print("File " + name + " is not a valid technology file.")
        return

#############################

def formattechtransfer(name, race = None):
    tabformat = ""
    if race:
        tabformat = "\t"
    output_lines.append(tabformat + "\t\tif = {")
    output_lines.append(tabformat + "\t\t\tlimit = {")
    output_lines.append(tabformat + "\t\t\t\tPREV = {")
    output_lines.append(tabformat + "\t\t\t\t\thas_tech = " + name + "")
    output_lines.append(tabformat + "\t\t\t\t}")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t\tset_technology = {")
    output_lines.append(tabformat + "\t\t\t\tpopup = no")
    output_lines.append(tabformat + "\t\t\t\t" + name + " = 1")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t}")

def formatpaperclip(name, race = None, doctrine = None):
    tabformat = ""
    if race:
        tabformat = "\t"
    output_lines.append(tabformat + "\t\tif = {")
    output_lines.append(tabformat + "\t\t\tlimit = {")
    output_lines.append(tabformat + "\t\t\t\tNOT = {")
    output_lines.append(tabformat + "\t\t\t\t\thas_tech = " + name + "")
    output_lines.append(tabformat + "\t\t\t\t}")
    output_lines.append(tabformat + "\t\t\t\tPREV = {")
    output_lines.append(tabformat + "\t\t\t\t\thas_tech = " + name + "")
    output_lines.append(tabformat + "\t\t\t\t}")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t\tset_variable = {")
    output_lines.append(tabformat + "\t\t\t\trand = random")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t\tmultiply_variable = {")
    output_lines.append(tabformat + "\t\t\t\trand = 100")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t\tround_variable = rand")
    output_lines.append(tabformat + "\t\t\tclamp_variable = {")
    output_lines.append(tabformat + "\t\t\t\tvar = rand")
    output_lines.append(tabformat + "\t\t\t\tmin = 0")
    output_lines.append(tabformat + "\t\t\t\tmax = 100")
    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t\tif = {")
    output_lines.append(tabformat + "\t\t\t\tlimit = {")
    output_lines.append(tabformat + "\t\t\t\t\tcheck_variable = {")
    output_lines.append(tabformat + "\t\t\t\t\t\tvar = rand")
    output_lines.append(tabformat + "\t\t\t\t\t\tvalue = PREV.PREV.previous_owner_industry_ratio")
    output_lines.append(tabformat + "\t\t\t\t\t\tcompare = less_than_or_equals")
    output_lines.append(tabformat + "\t\t\t\t\t}")
    output_lines.append(tabformat + "\t\t\t\t}")

    if doctrine:
        output_lines.append(tabformat + "\t\t\t\tadd_doctrine_cost_reduction = {")
        output_lines.append(tabformat + "\t\t\t\t\tname = paperclip_tech_bonus")
        output_lines.append(tabformat + "\t\t\t\t\tcost_reduction = 0.5")
        output_lines.append(tabformat + "\t\t\t\t\tuses = 1")
        output_lines.append(tabformat + f"\t\t\t\t\ttechnology = {name}")
        output_lines.append(tabformat + "\t\t\t\t}")
    else:
        output_lines.append(tabformat + "\t\t\t\tadd_tech_bonus = {")
        output_lines.append(tabformat + "\t\t\t\t\tname = paperclip_tech_bonus")
        output_lines.append(tabformat + "\t\t\t\t\tbonus = 2")
        output_lines.append(tabformat + "\t\t\t\t\tuses = 1")
        output_lines.append(tabformat + f"\t\t\t\t\ttechnology = {name}")
        output_lines.append(tabformat + "\t\t\t\t}")

    output_lines.append(tabformat + "\t\t\t}")
    output_lines.append(tabformat + "\t\t}")

#############################

parser = argparse.ArgumentParser(description='Given an input technology file or folder, generate a Transfer Technology scripted effect.')
parser.add_argument('input', metavar='input',
                    help='Technology file name/folder containing files')
parser.add_argument( 'output', metavar='output',
                    help='File name to write the scripted effect to')
parser.add_argument( '-en', '--effectname', metavar='effectname', default="transfer_technology", required=False,
                    help='Name of the scripted effect (default:\"transfer_technology\", paperclip default:\"paperclip_tech\")')
action = parser.add_mutually_exclusive_group(required=False)                    
action.add_argument( '-a', '--add', action='store_true',
                    help='Will add new technologies to an already existing transfer_technology effect (first set name with -en)')
action.add_argument( '-o', '--overwrite', action='store_true',
                    help='Will overwrite the output file if it already exists')
parser.add_argument( '-p', '--paperclip', action='store_true',
                    help='When creating for paperclip bonus effect')

args = parser.parse_args()
names_global = list()
names_race = list()
names_doctrine = list()
is_dir = False
try:
    dir = readable_dir(args.input)
    is_dir = True
except:
    print("Not a directory, treating as file.")

if is_dir:
    for file in glob.glob(dir+"/*.*"):
        parsed_file = readfile(file)
        filename = os.path.splitext(os.path.basename(file))[0]
        print(filename)
        if filename.endswith("doctrine"):
            names_doctrine = names_doctrine + parsed_file
            print("Added " + filename + " to doctrine list")
        elif filename.startswith("cat_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "cat")]
        elif filename.startswith("changeling_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "changeling")]
        elif filename.startswith("deer_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "deer")]
        elif filename.startswith("diamond_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "diamond_dog")]
        elif filename.startswith("generic_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "feneric")]
        elif filename.startswith("griffon_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "griffon")]
        elif filename.startswith("hippogriff_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "hippogriff")]
        elif filename.startswith("horse_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "horse")]
        elif filename.startswith("kirin_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "kirin")]
        elif filename.startswith("polar_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "polar")]
        elif filename.startswith("pony_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "pony")]
        elif filename.startswith("yak_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "yak")]
        elif filename.startswith("zebra_"):
            print("Added " + filename + " to race list")
            names_race = names_race + [(parsed_file, "zebra")]
        elif parsed_file:
            names_global = names_global + parsed_file
else:
    parsed_file = readfile(args.input)
    filename = os.path.splitext(os.path.basename(file))[0]
    print(filename)
    if filename.endswith("doctrine"):
        names_doctrine = names_doctrine + parsed_file
        print("Added " + filename + " to doctrine list")
    elif filename.startswith("cat_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "cat")]
    elif filename.startswith("changeling_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "changeling")]
    elif filename.startswith("deer_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "deer")]
    elif filename.startswith("diamond_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "diamond_dog")]
    elif filename.startswith("generic_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "feneric")]
    elif filename.startswith("griffon_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "griffon")]
    elif filename.startswith("hippogriff_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "hippogriff")]
    elif filename.startswith("horse_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "horse")]
    elif filename.startswith("kirin_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "kirin")]
    elif filename.startswith("polar_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "polar")]
    elif filename.startswith("pony_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "pony")]
    elif filename.startswith("yak_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "yak")]
    elif filename.startswith("zebra_"):
        print("Added " + filename + " to race list")
        names_race = names_race + [(parsed_file, "zebra")]
    elif parsed_file:
        names_global = names_global + parsed_file

if os.path.exists(args.output):
    if not args.overwrite and not args.add:
        sys.exit("File " + args.output + " already exists. Use -o parameter if you want to overwrite.")
elif args.add:
    sys.exit("File " + args.output + " doesn't exists. -a parameter requires an existing file.")

if args.add:
    with open(args.output,"r") as f:
        read_file = f.read()
        if not "### Automatically generated by Yard1's transfer_technology generator, originally for Equestria at War\n### File last modified: " in read_file:
            sys.exit("File " + args.output + " is not a vaild file to add to.")
        lines = read_file.splitlines()
        for line in lines:
            if "has_tech" in line:
                duplicate = re.sub("^\s*has_tech = ", "", line).strip()
                if duplicate in names_global:
                    names_global.remove(duplicate)
if not names_global or all(False for item in names_global):
    sys.exit("Nothing to add - every technology is already in " + args.output)    
output_lines = list()
if args.paperclip and args.effectname == "transfer_technology":
    args.effectname = "paperclip_tech"
if not args.add:
    output_lines.append("### DO NOT REMOVE OR CHANGE THE COMMENTS BELOW")
    output_lines.append("### Transfer Technology Effect (" + args.effectname + ")")
    output_lines.append("### Automatically generated by Yard1's transfer_technology generator, originally for Equestria at War")
    output_lines.append("### File last modified: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "")
    output_lines.append("### PREV is the giver, THIS is the reciever")

    output_lines.append(args.effectname + " = {")
    output_lines.append("\thidden_effect = {")

output_lines.append("")
if args.paperclip:
    for name in names_global:
        if name.endswith("_race"):
            continue
        formatpaperclip(name)
    for namerace in names_race:
        names, race = namerace
        output_lines.append("\t\tif = {")
        output_lines.append("\t\t\tlimit = {")
        output_lines.append("\t\t\t\thas_" + race + "_race_tech = yes")
        output_lines.append("\t\t\t}")
        for name in names:
            if name.endswith("_race"):
                continue
            formatpaperclip(name, race)
        output_lines.append("\t\t}")
    for name in names_doctrine:
        formatpaperclip(name, doctrine = True)
else:
    for name in names_global:
        if name.endswith("_race"):
            continue
        formattechtransfer(name)
    for namerace in names_race:
        names, race = namerace
        
        output_lines.append("\t\tif = {")
        output_lines.append("\t\t\tlimit = {")
        output_lines.append("\t\t\t\thas_" + race + "_race_tech = yes")
        output_lines.append("\t\t\t}")
        for name in names:
            if name.endswith("_race"):
                continue
            formattechtransfer(name, race)
        output_lines.append("\t\t}")
    for name in names_doctrine:
        formattechtransfer(name)

if not args.add:
    output_lines.append("\t}")
    output_lines.append("}")

if args.add:
    with open(args.output,"r+") as f:
        read_lines = f.read().splitlines()
        correct_format = False
        after_hidden_effect = False
        start_index = -1
        for i, line in enumerate(read_lines):
            if "### File last modified:" in line:
                read_lines[i] = "### File last modified: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if args.effectname + " = {" in line:
                correct_format = True
                continue
            if correct_format and "hidden_effect = {" in line:
                after_hidden_effect = True    
                continue
            if after_hidden_effect:
                start_index = i+1
                break
        for j, line in enumerate(output_lines):
            read_lines.insert(i+j, str(line))
        output_lines = read_lines 
print("Backuping " + args.output + "...")  
try:
    os.remove(args.output + '.bak')
    os.rename(args.output, args.output + '.bak')
except OSError:
    pass
print("Writing to " + args.output + "...")      
with open(args.output,"w+") as f:
    f.writelines(str(line) + "\n" for line in output_lines)
print("Written to " + args.output + " successfully!")         
print("Added " + str(len(names_global)) + " technologies.")
