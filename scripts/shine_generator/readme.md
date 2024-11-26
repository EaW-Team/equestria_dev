# General informations
## Summary
The aim of this script is to generate the shines associated with the the national focus GFX. At the same time, they are sorted in several following certain filters.
## File structures
A few files compose this program:
 * **shine_generator.py**: Main python program, contain all the code.
 * **requirements.txt**: *PIP* Packet dependencies to run the Python program.
 * **category.json**: The filters used to sort the GFX entries into several file.
## Program parameters
```
usage: shine_generator [-h] [-s] [-g GRAMMAR] [-d DATABASE] input output

Generate and sort the shine from an existing GFX file / folder

positional arguments:
  input                 The target file / folder with the existing GFX
  output                The folder that will be used as the output

options:
  -h, --help            show this help message and exit
  -s, --sort            The program will sort and regenerate the input GFX files if this option is activated
  -g GRAMMAR, --grammar GRAMMAR
                        Path to the TextX grammar file
  -d DATABASE, --database DATABASE
                        Path to the JSON containing the strings use to sort the GFX files
```
The program default to **category.json** for the database and ../pdx_grammar/pdx_script.tx" for the grammar file. As a normal user, it should not be needed to override these options.
## Category sorting
The **category.json** is a JSON file contain all the categories that is looked for. For exemple:
```
{
    "categories": {
        "EQS": ["EQS", "Equestrian", "SOLAR"],
        "DRG": ["DRG"],
        "OLE": ["OLE"],
        "CHN": ["CHN"],
        "YAK": ["YAK"],
        "GRF": ["GRF"]
    },
    "generic_name": "generic"
}
```
When parsing the GFX entries, the program will read each categories from top to bottom. It will check if the name of the GFX or the texture path contain any of the listed strings. If it does, then the entry is put in the category. If no category is found, it is put in the "generic_name" category. The case is ignored while checking the tokens.

GFX name is split in tokens using the "_" symbol, the texture path is split by the "/" symbol. For exemple:
```
spriteType = {
    name = GFX_EQS_toto # Give tokens ["GFX", "EQS", "toto"]
    texturePath = "ok/EQS/texture.tga" # Give tokens ["ok", "EQS", "texture.tga"]
}
```
If multiple categories are possible for one GFX entry, then the first category define in the file will be the one picked by the program.
# Program behavior and outputs
Here are the different execution step of the program:
 1. The program reads the file given as input parameter, or if it is a folder, read all the gfx file contained in the input folder.
 2. It then extracts all the GFX entries from the gfx file. A syntax check is performed a this step.
 3. Once all the file has been parsed, it will categorized all the GFX entries using the **category.json** as reference.
 4. The program creates the output folder if it does not exist yet, and generate all the shines files from the GFX entries. One shine file correspond to one category. An empty category does not generate a file
 5. If the option has been activated, it will recreate the GFX entries, sorted by category.

The output files organization is the following:
```
output_folder
|   -shine
|   |   - focus_category1_shine.gfx
|   |   - focus_category2_shine.gfx
|   |   ...
|   |   - focus_generic_shine.gfx
|   - focus_category1.gfx
|   - focus_category2.gfx
|   ...
|   - focus_generic.gfx
```
# Exemple
## Prerequisits and execution (Windows)
 * You need to first install [Python 3](https://www.python.org/downloads/release/python-3130/)
 * Open a powershell in the folder of the scripts by using Shift+Right Click on an empty space of the folder
 * Install the prerequisits using the **requirements.txt** file using the command `pip install -r requirements.txt`
 * You can then launch the script directly using `python -s shine_generator.py <input> <output_folder>`
  ## Case of a merge conflict
When merging from a branche that does not have yet this new organization, or if there are still conflict in the goals files, you need to manage these conflicts.

![Old GFX files](https://i.imgur.com/lb28Axq.png "Old GFX files")

The procedure is the following:
 1. Localize the GFX entries missing. In case of a deleted file, it is simply the new lines that have been added on the current branch compared to the incoming changes.
 2. Put this change in one of the current GFX file, no need to sort them
 3. Finish the merge
 4. Execute `python .\shine_generator.py -s ..\..\interface\focus ../../interface/focus`.
 5. Commit the new files

 ![New lines added in a file that doesn't exist anymore](https://i.imgur.com/LQlQZQx.png "New lines added in a file that doesn't exist anymore")
![The new GFX entry added in a random file]( https://i.imgur.com/8d3DXlr.png "The new GFX entry added in a random file")