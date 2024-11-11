from textx import metamodel_from_file
from textx.export import model_export
import pathlib
import os
import string
import argparse
import json

HEADER_GFX_FILE = """spriteTypes = {\n"""
FOOTER_GFX_FILE = """}"""
TEMPLATE_SPRITETYPE = """\tspritetype = {{
\t\tname = {name}
\t\ttextureFile = \"{texture}\"
\t}}
"""
TEMPLATE_SPRITETYPE_SHINE = """\tSpriteType = {{
\t\tname = "{name}_shine"
\t\ttexturefile = "{texture}"
\t\teffectFile = "gfx/FX/buttonstate.lua"
\t\tanimation = {{
\t\t\tanimationmaskfile = "{texture}"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.dds"
\t\t\tanimationrotation = -90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}

\t\tanimation = {{
\t\t\tanimationmaskfile = "{texture}"
\t\t\tanimationtexturefile = "gfx/interface/goals/shine_overlay.tga"
\t\t\tanimationrotation = 90.0
\t\t\tanimationlooping = no
\t\t\tanimationtime = 0.75
\t\t\tanimationdelay = 0
\t\t\tanimationblendmode = "add"
\t\t\tanimationtype = "scrolling"
\t\t\tanimationrotationoffset = {{ x = 0.0 y = 0.0 }}
\t\t\tanimationtexturescale = {{ x = 1.0 y = 1.0 }}
\t\t}}
\t\tlegacy_lazy_load = no
\t}}"""
TEMPLATE_GFX_FILENAME = "focus_{name}.gfx"
SHINE_FOLDER_NAME = "shine"
TEMPLATE_SHINE_GFX_FILENAME = "focus_{name}_shine.gfx"

# Default paths, generated from the current script path
current_folder_path = pathlib.Path().resolve()
DEFAULT_GRAMMAR_PATH = os.path.join(current_folder_path, "..", "pdx_grammar", "pdx_scripts.tx")
DEFAULT_DATABASE_PATH = os.path.join(current_folder_path, "category.json")

# CLI arguments management
parser = argparse.ArgumentParser(
    prog="shine_generator",
    description="Generate and sort the shine from an existing GFX file / folder")

parser.add_argument("input", help="The target file / folder with the existing GFX")
parser.add_argument("output", help="The folder that will be used as the output")
parser.add_argument("-s", "--sort",
                    help="The program will sort and regenerate the input GFX files if this option is activated",
                    action="store_true")
parser.add_argument("-g", "--grammar",
                    help="Path to the TextX grammar file",
                    default=DEFAULT_GRAMMAR_PATH,
                    nargs=1)
parser.add_argument("-d", "--database",
                    help="Path to the JSON containing the strings use to sort the GFX files",
                    default=DEFAULT_DATABASE_PATH,
                    nargs=1)

def parse_spritetype(model):
    name = None
    texture = None
    for key in model.value.elements:
        if key.name.upper() == "NAME":
            name = key.value
        if key.name.upper() == "TEXTUREFILE":
            texture = key.value
    return (name, texture) if name and texture else None

def check_category(gfx_name, texture_name, categories_filters):
    res = []
    tokens = set(gfx_name.upper().split("_"))
    tokens_texture = set(texture_name.upper().split("/"))
    for category, filters in categories_filters.items():
        for filter in filters:
            if filter.upper() in tokens or filter.upper() in tokens_texture:
                res.append(category)
                continue
    return res

def generate_gfx_file(folder_path, list_gfx, categories):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for category, gfx_names in categories.items():
        if not len(gfx_names):
            continue
        with open(os.path.join(folder_path, TEMPLATE_GFX_FILENAME.format(name=category)), "w") as fd:
            fd.write(HEADER_GFX_FILE)

            list_category_gfx = list(gfx_names)
            list_category_gfx.sort()
            for gfx_name in list_category_gfx:
                fd.write(TEMPLATE_SPRITETYPE.format(name=gfx_name, texture=list_gfx[gfx_name]))

            fd.write(FOOTER_GFX_FILE)


def generate_shine_gfx_file(folder_path, list_gfx, categories):
    if not os.path.exists(os.path.join(folder_path, SHINE_FOLDER_NAME)):
        os.makedirs(os.path.join(folder_path, SHINE_FOLDER_NAME), exist_ok=True)

    for category, gfx_names in categories.items():
        if not len(gfx_names):
            continue
        with open(os.path.join(folder_path, SHINE_FOLDER_NAME, TEMPLATE_SHINE_GFX_FILENAME.format(name=category)), "w") as fd:
            fd.write(HEADER_GFX_FILE)

            list_category_gfx = list(gfx_names)
            list_category_gfx.sort()
            for gfx_name in list_category_gfx:
                fd.write(TEMPLATE_SPRITETYPE_SHINE.format(name=gfx_name, texture=list_gfx[gfx_name]))

            fd.write(FOOTER_GFX_FILE)

def main():
    args = parser.parse_args()

    # Open the grammar and the target
    pdx_meta = metamodel_from_file(args.grammar)

    # Get all the gfx files
    list_gfx = {} # A dict with the name as key and path as data for each of the GFX
    set_gfx = set()
    input_files = list(pathlib.Path(args.input).glob('*.gfx'))
    for file_name in input_files:
        model = pdx_meta.model_from_file(str(file_name))
        # Find the root spriteTypes
        for key in model.elements:
            if key.name.upper() == "SPRITETYPES":
                for element in key.value.elements:
                    if element.name.upper() == "SPRITETYPE":
                        tupple = parse_spritetype(element)
                        if not tupple:
                            print("Malformed SpiritType")
                        else:
                            list_gfx[tupple[0]] = tupple[1]
                        if tupple[0] in set_gfx:
                            print(f"Redefinition of {tupple[0]}")
                        set_gfx.add(tupple[0])

    # Now parse the database
    with open(args.database) as fp:
        database = json.load(fp)
    categories = database["categories"]
    generic_name = database["generic_name"]

    # Prepare the list of GFX
    categories_content_list = {generic_name: set()}
    for elmt in categories:
        categories_content_list[elmt] = set()

    for name, texture in list_gfx.items():
        res = check_category(name, texture, categories)
        if res and len(res) > 1:
            print(f"Multiple filter hits for {name}, {res}. Put in {res[0]}")
        if res:
            categories_content_list[res[0]].add(name)
        else:
            categories_content_list[generic_name].add(name)

    #for elmt in categories_content_list[generic_name]:
    #    print(elmt)
    for key, elmt in categories_content_list.items():
        if len(elmt) > 0:
            print(f"{key}: nb elements {len(elmt)}")

    # If sort activated, regeneration of input files
    if args.sort:
        generate_gfx_file(args.output, list_gfx, categories_content_list)

    generate_shine_gfx_file(args.output, list_gfx, categories_content_list)
if __name__ == "__main__":
    main()