import os
import re
import sys
import json
import subprocess
import argparse
from collections import defaultdict
from wand import image  # also requires apt-get install libmagickwand-dev
from wand.api import library


def convert_images(paths, updated_images=None):
    for x in paths:
        for path in x:
            if os.path.exists(path):
                if updated_images and not path in updated_images:
                    continue
                fname = os.path.splitext(path)[0]
                with image.Image(filename=path) as img:
                    library.MagickSetCompressionQuality(img.wand, 95)
                    print("Saving %s..." % (fname + '.png'))
                    img.save(filename=fname + '.png')
            else:
                print("%s does not exist!" % path)


def read_gfx(gfx_paths):
    gfx = {}
    gfx_files = defaultdict(list)
    for path in gfx_paths:
        path = os.path.join(path)
        with open(path, 'r') as f:
            lines = f.readlines()
        name = ''
        texturefile = ''
        for line in lines:
            line = re.sub(r'#.*', '', line)
            match = re.match(r'\s*name\s*=\s*"(.+?)"\s*$', line)
            if match:
                name = match.group(1)
                continue
            if name:
                match = re.match(r'\s*texturefile\s*=\s*"(.+?)"\s*$', line)
                if match:
                    texturefile = match.group(1)
            if texturefile:
                gfx[name] = texturefile
                gfx_files[os.path.normpath(texturefile)].append(name)
                name = ''
                texturefile = ''
    return (gfx, gfx_files)


def generate_html(goals, ideas, texticons, events, decisions, title, favicon):
    with open(os.path.join('.github-pages', 'index.template'), 'r') as f:
        html = f.read()

    goal_entries = []
    goals_num = 0

    for goal, path in goals.items():
        img_src = os.path.splitext(path)[0] + '.png'
        if os.path.exists(img_src):
            goals_num += 1
            goal_entries.append('''
          <div data-clipboard-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (goal, goal, img_src, goal))

    html = html.replace('@GOALS_ICONS', ''.join(goal_entries))
    html = html.replace('@GOALS_NUM', str(goals_num))

    idea_entries = []
    ideas_num = 0

    for idea, path in ideas.items():
        img_src = os.path.splitext(path)[0] + '.png'
        if os.path.exists(img_src):
            ideas_num += 1
            idea_entries.append('''
          <div data-clipboard-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (idea, idea, img_src, idea))

    html = html.replace('@IDEAS_ICONS', ''.join(idea_entries))
    html = html.replace('@IDEAS_NUM', str(ideas_num))

    texticons_entries = []
    texticons_num = 0

    for texticon, path in texticons.items():
        img_src = os.path.splitext(path)[0] + '.png'
        if os.path.exists(img_src):
            texticons_num += 1
            texticons_entries.append('''
          <div data-clipboard-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (texticon, texticon, img_src, texticon))

    html = html.replace('@TEXTICONS_ICONS', ''.join(texticons_entries))
    html = html.replace('@TEXTICONS_NUM', str(texticons_num))

    events_entries = []
    events_num = 0

    for event, path in events.items():
        img_src = os.path.splitext(path)[0] + '.png'
        if os.path.exists(img_src):
            events_num += 1
            events_entries.append('''
          <div data-clipboard-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (event, event, img_src, event))

    html = html.replace('@EVENTS_ICONS', ''.join(events_entries))
    html = html.replace('@EVENTS_NUM', str(events_num))

    decisions_entries = []
    decisions_num = 0

    for decision, path in decisions.items():
        img_src = os.path.splitext(path)[0] + '.png'
        if os.path.exists(img_src):
            decisions_num += 1
            decisions_entries.append('''
          <div data-clipboard-text="%s" title="%s" class="icon">
            <img src="%s" alt="%s">
          </div>
        ''' % (decision, decision, img_src, decision))

    html = html.replace('@DECISIONS_ICONS', ''.join(decisions_entries))
    html = html.replace('@DECISIONS_NUM', str(decisions_num))

    html = html.replace('@TITLE', title)
    favicon = favicon if favicon else ""
    html = html.replace('@FAVICON', favicon)

    with open('index.html', 'w') as f:
        f.write(html)


def main():
    print("Starting hoi4_icon_search_gen...")
    args = setup_cli_arguments()
    if args.modified_images:
        args.modified_images = set(args.modified_images)
        print(args.modified_images)
    goals, goals_files = read_gfx(args.goals)
    ideas, ideas_files = read_gfx(args.ideas)
    texticons, texticons_files = read_gfx(args.texticons)
    events, events_files = read_gfx(args.events)
    decisions, decisions_files = read_gfx(args.decisions)
    convert_images([goals_files.keys(), ideas_files.keys(), texticons_files.keys(), events_files.keys(), decisions_files.keys()],
                   args.modified_images)
    generate_html(goals, ideas, texticons, events, decisions, args.title, args.favicon)


def setup_cli_arguments():
    parser = argparse.ArgumentParser(
        description='')
    parser.add_argument('--goals', nargs='*',
                        help='Paths to goals (national focus) interface gfx files', required=True)
    parser.add_argument('--ideas', nargs='*',
                        help='Paths to ideas interface gfx files', required=True)
    parser.add_argument('--texticons', nargs='*',
                        help='Paths to texticons interface gfx files', required=True)
    parser.add_argument('--events', nargs='*',
                        help='Paths to events interface gfx files', required=True)
    parser.add_argument('--decisions', nargs='*',
                        help='Paths to decisions interface gfx files', required=True)
    parser.add_argument('--title',
                        help='Webpage title', required=True)
    parser.add_argument('--favicon',
                        help='Path to webpage favicon', required=False)
    parser.add_argument('--modified-images', nargs='*',
                        help='Paths to modified image files (If not set, will convert all images)', dest="modified_images", required=False)

    args = parser.parse_args()
    args.goals = [os.path.normpath(x) for x in args.goals] if args.goals else []
    args.ideas = [os.path.normpath(x) for x in args.ideas] if args.ideas else []
    args.texticons = [os.path.normpath(x) for x in args.texticons] if args.texticons else []
    args.events = [os.path.normpath(x) for x in args.events] if args.events else []
    args.decisions = [os.path.normpath(x) for x in args.decisions] if args.decisions else []
    if args.modified_images:
        args.modified_images = [os.path.normpath(
            x) for x in args.modified_images]
    return args


if __name__ == "__main__":
    main()
