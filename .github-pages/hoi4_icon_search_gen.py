import os
import re
import sys
import json
import subprocess
import argparse
import datetime
import traceback
from collections import defaultdict
from wand import image  # also requires apt-get install libmagickwand-dev
from wand.api import library

BAD_FILES = []

def convert_images(paths, updated_images=None):
    global BAD_FILES
    for x in paths:
        for path, value in x.items():
            frames = value[0].frames
            if updated_images and not path in updated_images:
                continue
            try:
                convert_image(path, frames)
            except:
                print("EXCEPTION with %s" % path)
                ex_message = traceback.format_exc()
                BAD_FILES.append((path, ex_message))
                print(ex_message)

def convert_image(path, frames):
    if os.path.exists(path):
        fname = os.path.splitext(path)[0]
        with image.Image(filename=path) as img:
            if frames > 1:
                print("%s has %d frames, cropping..." % (fname, frames))
                img.crop(0, 0, width=img.width // frames, height=img.height)
            library.MagickSetCompressionQuality(img.wand, 00)
            new_fname = fname + '.png'
            print("Saving %s..." % (new_fname))
            img.save(filename=new_fname)
            return new_fname
    else:
        print("%s does not exist!" % path)
        return None

class SpriteType:
    def __init__(self, name, texturefile, frames):
        self.name = name
        self.texturefile = texturefile
        self.frames = frames

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

def read_gfx(gfx_paths):
    gfx = {}
    gfx_files = defaultdict(list)
    for path in gfx_paths:
        path = os.path.join(path)
        with open(path, 'r') as f:
            file_contents = f.read()
        file_contents = re.sub(r'#.*\n', ' ', file_contents, re.IGNORECASE)
        file_contents = file_contents.replace('\n', ' ')
        spriteTypes = re.findall(r'spriteType\s*=\s*\{[^\{\}]*?\}', file_contents, re.IGNORECASE)
        for spriteType in spriteTypes:
            name = ''
            texturefile = ''
            noOfFrames = 1
            match = re.search(r'\s+name\s*=\s*\"(.+?)\"', spriteType, re.IGNORECASE)
            if match:
                name = match.group(1)
            match = re.search(r'\s+texturefile\s*=\s*\"(.+?)\"', spriteType, re.IGNORECASE)
            if match:
                texturefile = os.path.normpath(match.group(1))
            match = re.search(r'\s+noOfFrames\s*=\s*([0-9]+?)', spriteType, re.IGNORECASE)
            if match:
                noOfFrames = int(match.group(1))
            if name and texturefile:
                st = SpriteType(name, texturefile, noOfFrames)
                gfx[name] = st
                gfx_files[texturefile].append(st)

    return (gfx, gfx_files)

def generate_icons_section(icons_dict, path_dicts, remove_str = None):
    global BAD_FILES
    icon_entries = []
    icons_num = 0

    for key, icon in icons_dict.items():
        name = icon.name
        path = icon.texturefile
        img_src = os.path.splitext(path)[0] + '.png'
        if not os.path.exists(img_src):
            try:
                frames = icon.frames
                convert_image(path, frames)
            except:
                print("EXCEPTION with %s" % path)
                ex_message = traceback.format_exc()
                BAD_FILES.append((path, ex_message))
                print(ex_message)
        if os.path.exists(img_src):
            if remove_str:
                name = name.replace(remove_str, "")
            icons_num += 1
            icon_entries.append('''
          <div data-clipboard-text="%s" data-search-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (name, name, name, img_src, name))
    return (icon_entries, icons_num)

def generate_html(goals, ideas, texticons, events, news_events, agencies, decisions, decisions_cat, decisions_pics, path_dicts, title, favicon):
    with open(os.path.join('.github-pages', 'index.template'), 'r') as f:
        html = f.read()

    goal_entries, goals_num = generate_icons_section(goals, path_dicts)

    html = html.replace('@GOALS_ICONS', ''.join(goal_entries))
    html = html.replace('@GOALS_NUM', str(goals_num))

    idea_entries, ideas_num = generate_icons_section(ideas, path_dicts, "GFX_idea_")

    html = html.replace('@IDEAS_ICONS', ''.join(idea_entries))
    html = html.replace('@IDEAS_NUM', str(ideas_num))

    texticons_entries, texticons_num = generate_icons_section(texticons, path_dicts)

    html = html.replace('@TEXTICONS_ICONS', ''.join(texticons_entries))
    html = html.replace('@TEXTICONS_NUM', str(texticons_num))

    events_entries, events_num = generate_icons_section(events, path_dicts)

    html = html.replace('@EVENTS_ICONS', ''.join(events_entries))
    html = html.replace('@EVENTS_NUM', str(events_num))

    news_events_entries, news_events_num = generate_icons_section(news_events, path_dicts)

    html = html.replace('@NEWSEVENTS_ICONS', ''.join(news_events_entries))
    html = html.replace('@NEWSEVENTS_NUM', str(news_events_num))

    agencies_entries, agencies_num = generate_icons_section(agencies, path_dicts)

    html = html.replace('@AGENCIES_ICONS', ''.join(agencies_entries))
    html = html.replace('@AGENCIES_NUM', str(agencies_num))

    decisions_entries, decisions_num = generate_icons_section(decisions, path_dicts)

    html = html.replace('@DECISIONS_ICONS', ''.join(decisions_entries))
    html = html.replace('@DECISIONS_NUM', str(decisions_num))

    decisions_cat_entries, decisions_cat_num = generate_icons_section(decisions_cat, path_dicts)

    html = html.replace('@DECISIONSCAT_ICONS', ''.join(decisions_cat_entries))
    html = html.replace('@DECISIONSCAT_NUM', str(decisions_cat_num))

    decisions_pics_entries, decisions_pics_num = generate_icons_section(decisions_pics, path_dicts)

    html = html.replace('@DECISIONSPICS_ICONS', ''.join(decisions_pics_entries))
    html = html.replace('@DECISIONSPICS_NUM', str(decisions_pics_num))

    html = html.replace('@TITLE', title)
    favicon = favicon if favicon else ""
    html = html.replace('@FAVICON', favicon)
    #html = html.replace('@UPDATE_DATE', str(datetime.datetime.utcnow())) # moved to the action itself so it can only be updated on push

    with open('index.html', 'w') as f:
        f.write(html)


def main():
    global BAD_FILES
    print("Starting hoi4_icon_search_gen...")
    args = setup_cli_arguments()
    if args.modified_images:
        args.modified_images = set(args.modified_images)
        print(args.modified_images)
    goals, goals_files = read_gfx(args.goals)
    ideas, ideas_files = read_gfx(args.ideas)
    texticons, texticons_files = read_gfx(args.texticons)
    events, events_files = read_gfx(args.events)
    news_events, news_events_files = read_gfx(args.news_events)
    agencies, agencies_files = read_gfx(args.agencies)
    decisions, decisions_files = read_gfx(args.decisions)
    decisions_cat, decisions_cat_files = read_gfx(args.decisions_cat)
    decisions_pics, decisions_pics_files = read_gfx(args.decisions_pics)
    path_dicts = [goals_files, ideas_files, texticons_files, events_files, news_events_files, agencies_files, decisions_files, decisions_cat_files, decisions_pics_files]
    convert_images(path_dicts,
                   args.modified_images)
    generate_html(goals, ideas, texticons, events, news_events, agencies, decisions, decisions_cat, decisions_pics, path_dicts, args.title, args.favicon)
    print("The following files had exceptions:")
    for f in BAD_FILES:
        print(f[0])
        print(f[1])

def setup_cli_arguments():
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--goals', nargs='*',
                        help='Paths to goals (national focus) interface gfx files', required=False)
    parser.add_argument('--ideas', nargs='*',
                        help='Paths to ideas interface gfx files', required=False)
    parser.add_argument('--texticons', nargs='*',
                        help='Paths to texticons interface gfx files', required=False)
    parser.add_argument('--events', nargs='*',
                        help='Paths to events interface gfx files', required=False)
    parser.add_argument('--news-events', nargs='*', dest="news_events",
                        help='Paths to news events interface gfx files', required=False)
    parser.add_argument('--agencies', nargs='*',
                        help='Paths to agencies interface gfx files', required=False)
    parser.add_argument('--decisions', nargs='*',
                        help='Paths to decisions interface gfx files', required=False)
    parser.add_argument('--decisions-cat', nargs='*', dest="decisions_cat",
                        help='Paths to decisions category interface gfx files', required=False)
    parser.add_argument('--decisions-pics', nargs='*', dest="decisions_pics",
                        help='Paths to decision category picture interface gfx files', required=False)
    parser.add_argument('--title',
                        help='Webpage title', required=True)
    parser.add_argument('--favicon',
                        help='Path to webpage favicon', required=False)
    parser.add_argument('--modified-images', nargs='*',
                        help='Paths to modified image files (If not set, will convert all images)', dest="modified_images", required=False)
    parser.add_argument('--modified-images-str', nargs='?',
                        help='Paths to modified image files (If not set, will convert all images)', dest="modified_images_str", required=False)

    args = parser.parse_args()
    args.goals = [os.path.normpath(x) for x in args.goals] if args.goals else []
    args.ideas = [os.path.normpath(x) for x in args.ideas] if args.ideas else []
    args.texticons = [os.path.normpath(x) for x in args.texticons] if args.texticons else []
    args.events = [os.path.normpath(x) for x in args.events] if args.events else []
    args.news_events = [os.path.normpath(x) for x in args.news_events] if args.news_events else []
    args.agencies = [os.path.normpath(x) for x in args.agencies] if args.agencies else []
    args.decisions = [os.path.normpath(x) for x in args.decisions] if args.decisions else []
    args.decisions_cat = [os.path.normpath(x) for x in args.decisions_cat] if args.decisions_cat else []
    args.decisions_pics = [os.path.normpath(x) for x in args.decisions_pics] if args.decisions_pics else []
    if args.modified_images_str:
        args.modified_images_str = [x.replace("'", "") for x in re.findall(r"'[^']+'", args.modified_images_str)]
        args.modified_images = args.modified_images_str
    if args.modified_images:
        args.modified_images = [os.path.normpath(
            x) for x in args.modified_images]
    return args


if __name__ == "__main__":
    main()
