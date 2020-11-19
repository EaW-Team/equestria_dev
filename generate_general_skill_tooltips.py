#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path
import re
from collections import defaultdict
from unidecode import unidecode
global_loc = {}


def strip_comments(txt: str) -> str:
    comments = re.finditer(r"#.*$", txt, re.MULTILINE)
    for match in comments:
        txt = txt[:match.start(0)] + " " * (match.end(0) - match.start(0)) + txt[match.end(0):]
    return txt

def strip_hidden_effect(txt:str) -> str:
    matches = re.finditer(r"hidden_effect\s*=\s*\{", txt, re.DOTALL | re.IGNORECASE)
    hidden_effect_blocks = [find_brackets_block(txt, match.end(0)) for match in matches]
    for start, end in hidden_effect_blocks:
        txt = txt[:start] + " " * (end - start) + txt[end:]
    return txt

def clean_script(txt:str) -> str:
    return strip_hidden_effect(strip_comments(txt))

def find_brackets_block(txt: str, end:int) -> list:
    unclosed_brackets = 0
    starting_index = end-1
    ending_index = starting_index
    for char in txt[starting_index:]:
        if char == "{":
            unclosed_brackets += 1
        elif char == "}":
            unclosed_brackets -= 1
        ending_index += 1
        if unclosed_brackets == 0:
            return (starting_index, ending_index)

def find_create_unit_leader(txt: str) -> list:
    matches = re.finditer(r"(\s*)((?:(?:create_corps_commander)|(?:create_field_marshal)|(?:create_navy_leader))\s*=\s*\{)", txt, re.DOTALL | re.IGNORECASE)
    return [list(find_brackets_block(txt, match.end(2))) + [match.start(2), match.group(1)] for match in matches]

def check_for_custom_effect_tooltip(txt: str, end:int) -> re.Match:
    return re.match(r"\s*custom_effect_tooltip\s*=\s*\w+", txt[end:], re.MULTILINE)

def get_leader_blocks_from_file(path):
    print(f"Reading file {path}")
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    if "create_corps_commander" in txt or "create_field_marshal" in txt or "create_navy_leader" in txt:
        stripped_txt = clean_script(txt)
        create_unit_leader_blocks = find_create_unit_leader(stripped_txt)
        create_unit_leader_blocks_no_tooltip = []
        create_unit_leader_blocks_tooltip = []
        for start, end, start_t, indents in create_unit_leader_blocks:
            cet_match = check_for_custom_effect_tooltip(stripped_txt, end)
            if cet_match:
                create_unit_leader_blocks_tooltip.append((start_t, start, end, cet_match.group(0)))
            else:
                create_unit_leader_blocks_no_tooltip.append((start_t, start, end))
        if create_unit_leader_blocks_tooltip:
            create_unit_leader_blocks_tt_global[path] = create_unit_leader_blocks_tooltip
        if create_unit_leader_blocks_no_tooltip:
            create_unit_leader_blocks_global[path] = create_unit_leader_blocks_no_tooltip

class CreateUnitLeader():
    name = ""
    skill = ""
    loc_key = ""
    
    def get_stats(self):
        return

    def get_skill(self):
        if not self.skill:
            self.skill = int(re.search(r"skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        return self.skill

    def get_name(self):
        if not self.name:
            self.name = re.search(r"name\s*=\s*\"([^\"]+)\"", self.text, re.DOTALL | re.IGNORECASE).group(1)
        return self.name

    def get_loc_key(self):
        if not self.loc_key:
            name = self.get_name().strip().replace(" ", "_").lower().replace("'", "").replace(".", "")
            name = unidecode(name)
            self.loc_key = f"{name}_stats_tp"
            loc_key = self.loc_key
            i = 1
            if not (loc_key in global_loc and global_loc[loc_key] == str(self)):
                while loc_key in global_loc:
                    loc_key = f"{self.loc_key}_{i}"
                    i+=1
                self.loc_key = loc_key
                global_loc[loc_key] = str(self)
            self.loc_key = loc_key
        return self.loc_key

    def __init__(self, txt:str, start:int, end:int, tt:str = ""):
        self.end = end
        self.text = txt[start+1:end-1]
        self.tooltip = tt

class CreateLandLeader(CreateUnitLeader):
    attack = ""
    defense = ""
    planning = ""
    logistics = ""

    def get_stats(self):
        try:
            if not self.attack:
                self.attack = int(re.search(r"attack_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.attack = 1
        try:
            if not self.defense:
                self.defense = int(re.search(r"defense_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.defense = 1
        try:
            if not self.planning:
                self.planning = int(re.search(r"planning_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.planning = 1
        try:
            if not self.logistics:
                self.logistics = int(re.search(r"logistics_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.logistics = 1
        return (self.attack, self.defense, self.planning, self.logistics)
    
    def __str__(self):
        self.get_stats()
        return f"{self.get_loc_key()}:0 \"§RAttack Skill§!: §Y{self.attack}§!\\n§YDefense Skill§!: §Y{self.defense}§!\\n§GPlanning Skill§!: §Y{self.planning}§!\\n§CLogistics Skill§!: §Y{self.logistics}§!\\n\\n\""

class CreateNavyLeader(CreateUnitLeader):
    attack = ""
    defense = ""
    maneuvering = ""
    coordination = ""

    def get_stats(self):
        try:
            if not self.attack:
                self.attack = int(re.search(r"attack_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.attack = 1
        try:
            if not self.defense:
                self.defense = int(re.search(r"defense_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.defense = 1
        try:
            if not self.maneuvering:
                self.maneuvering = int(re.search(r"maneuvering_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.maneuvering = 1
        try:
            if not self.coordination:
                self.coordination = int(re.search(r"coordination_skill\s*=\s*([0-9]+)", self.text, re.DOTALL | re.IGNORECASE).group(1))
        except:
            self.coordination = 1
        return (self.attack, self.defense, self.maneuvering, self.coordination)

    def __str__(self):
        self.get_stats()
        return f"{self.get_loc_key()}:0 \"§RAttack Skill§!: §Y{self.attack}§!\\n§YDefense Skill§!: §Y{self.defense}§!\\n§GManeuvering Skill§!: §Y{self.maneuvering}§!\\n§CCoordination Skill§!: §Y{self.coordination}§!\\n\\n\""

def make_create_leader(txt:str, start_t:int, start:int, end:int, tt:str="") -> CreateUnitLeader:
    if re.match(r"\s*create_navy_leader", txt[start_t:start]):
        return CreateNavyLeader(txt,start,end,tt)
    else:
        return CreateLandLeader(txt,start,end,tt)

#for path in Path('common').rglob('*.txt'):
create_unit_leader_blocks_global = {}
create_unit_leader_blocks_tt_global = {}
for path in Path('common').rglob('*.txt'):
    get_leader_blocks_from_file(path)

for path in Path('events').rglob('*.txt'):
    get_leader_blocks_from_file(path)

create_unit_leader_blocks_class_global = defaultdict(list)
create_unit_leader_blocks_tt_class_global = defaultdict(list)

for path,v in create_unit_leader_blocks_tt_global.items():
    for start_t,start,end,tt in v:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
        create_unit_leader_blocks_tt_class_global[path].append(make_create_leader(txt, start_t, start, end,tt))
        print(str(create_unit_leader_blocks_tt_class_global[path][-1]))

global_loc = {}

for path,v in create_unit_leader_blocks_global.items():
    for start_t,start,end in v:
        with open(path, "r", encoding="utf-8") as f:
            txt = f.read()
        create_unit_leader_blocks_class_global[path].append(make_create_leader(txt, start_t, start, end))

for path, v in create_unit_leader_blocks_class_global.items():
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read()
    offset = 0
    for x in v:
        lkey = f" custom_effect_tooltip = {x.get_loc_key()}"
        txt = txt[:x.end+offset] + lkey + txt[x.end+offset:]
        offset+=len(lkey)
    with open(path, "w", encoding="utf-8") as f:
        f.write(txt)

for v in sorted(list(global_loc.values())):
    print(v)