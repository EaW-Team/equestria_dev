#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import os
import sys
import re
import collections
import io
import functools 

def get_clean_dct(fname):
    with io.open(fname, 'r', encoding='utf8') as f:
        text = f.readlines()

    dct = {}
    entry = []
    current_name = ""
    for line in text:
        txt = re.sub(r"#.*", "", line)
        txt = re.sub(r"^\s*$", "", txt)
        if txt:
            entry.append(txt)
        match = re.search(r"\s*name\s*=\s*(.+)", txt)
        if match:
            current_name = match.group(1).strip()
        match = re.match(r"[A-Z]{3}", txt)
        if match:
            current_name = match.group(0).strip()
        match = re.match(r"^}", txt)
        if match:
            dct[current_name] = entry.copy()
            entry = []

    duplicates = set()
    for key, value in dct.items():
        for key2, value2 in dct.items():
            if key != key2 and not key in duplicates and not key2 in duplicates:
                if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, value[2:], value2[2:]), True):
                    duplicates.add(key2)
    for d in duplicates:
        dct.pop(d)

    print(duplicates)
    clean_dct = {}

    for key, value in dct.items():
        cat = ""
        gender = ""
        entry = []
        for line in value:
            if cat and gender and re.search(r"}", line):
                k = "%s_%s_%s" % (key, cat, gender)
                clean_dct[k] = entry.copy()
                entry = []
                gender = ""
            if cat and gender and not re.search(r"{", line):
                entry.append(line.strip())
            match = re.match(r"\s*(army|navy|operative)", line)
            if match:
                cat = match.group(1)
            match = re.match(r"\s*(female|male)", line)
            if cat and match:
                gender = match.group(1)
    return clean_dct

def generate_sl(clean_dict):
    duplicates = set()
    for key, value in clean_dict.items():
        for key2, value2 in clean_dict.items():
            if key != key2 and not key in duplicates and not key2 in duplicates:
                if functools.reduce(lambda i, j : i and j, map(lambda m, k: m == k, value, value2), True):
                    if re.search(r"(africa|asia|europe)", key):
                        duplicates.add(key2)
                    else:
                        duplicates.add(key)
    for d in duplicates:
        clean_dict.pop(d)
    print(duplicates)
    out = []
    for tag, types in clean_dct.items():
        if len(types) < 1:
            continue
        entry = '''    defined_text = { #max %d
        name = Get_%s
    ''' % (len(types), tag)
        for idx, name in enumerate(types):
            entry += '''    text = {
            trigger = { check_variable = { THIS = %d } }
            localization_key = "GFX_%s_portrait"
        }
    ''' % (idx+1, re.search(r"([^/\.]+)\.", name).group(1))
        entry += "}"
        out.append(entry)
    return out


clean_dct = get_clean_dct("portraits/eaw_portraits.txt")
clean_dct_o = get_clean_dct("portraits/eaw_operative_portraits.txt")
out = ["spriteTypes = {"]
st = set()
for key, value in clean_dct.items():
    for x in value:
        st.add(x)

for key, value in clean_dct_o.items():
    for x in value:
        st.add(x)

for x in sorted(st):
    txt = '''    spriteType = {
        name = "GFX_%s"
        textureFile = %s
    }''' % (re.search(r"([^/\.]+)\.", x).group(1), x)
    out.append(txt)

out.append("}")

with io.open("out_gfx.gfx", 'w', encoding='utf8') as f:
    f.write("\n".join(out))

dct = clean_dct
dct.update(clean_dct_o)

out = []
out.extend(generate_sl(dct))

with io.open("out.txt", 'w', encoding='utf8') as f:
    f.write("\n".join(out))