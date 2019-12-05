# *-* encoding: utf-8 -*-
#!/usr/bin/env python
"""
Usage:
  mp3chaps.py -i <mp3file> -c <chaptersfile>
  mp3chaps.py -l <mp3file>

Options:
  -l  List chapters in <filename>
  -i  Import chapters
      Example: mp3chaps.py -i <mp3file> -c <chaptersfile>
"""
from argparse import ArgumentParser
from eyed3.id3 import Tag
from eyed3 import core
from docopt import docopt
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

argp = ArgumentParser(
    prog = 'mp3chaps',
    description = '',
    epilog = 'GPL v3.0',
)

def show_chapters(tag):
    "list chapters in tag"
    print("Chapters:")
    for chap in tag.chapters:
        print(chap.sub_frames.get(b"TIT2")[0]._text)

def to_millisecs(time):
  h, m, s = [float(x) for x in time.split(":")]
  return int(1000 * (s + m*60 + h*60*60))

def main(mp3file, chaptersfile):
    total_length = int(core.load(mp3file).info.time_secs * 1000)
    chapters = []
    n = 0

    tag = Tag()
    tag.parse(mp3file)
    for i in open(chaptersfile,'r').readlines():
        chapter_time = to_millisecs(i[0:12])
        chapter_title = u'{}'.format(i[13:]).rstrip()
        chapters.append([[chapter_time,0], chapter_title, 'ch_'+str(n)])
        if n > 0: chapters[n-1][0][1] = chapter_time
        n+=1
    chapters[n-1][0][1] = total_length
    for times, title, id in chapters:
        chapter_frame = tag.chapters.set(id, tuple(times))
        chapter_frame.sub_frames.setTextFrame(b"TIT2", title)
    tag.table_of_contents.set(
        'toc',
        child_ids=[e[2] for e in chapters]
    )
    show_chapters(tag)
    tag.save()

argp.add_argument('-i', help='mp3 file input')
argp.add_argument('-l', help='show a chapter list')
argp.add_argument('-c', help='chapters file input')
args = vars(argp.parse_args())

if args['i']:
    mp3file = args['i']
    chaptersfile = args['c']
    if mp3file and chaptersfile:
        if not os.path.isfile(mp3file):
            argp.error('File {} not exists'.format(mp3file))
        if not os.path.isfile(chaptersfile):
            argp.error('File {} not exists'.format(chaptersfile))
        main(mp3file, chaptersfile)
    else:
        argp.print_help()
elif args['l']:
    mp3file = args['l']
    if mp3file:
        tag = Tag()
        tag.parse(mp3file)
        show_chapters(tag)
    else:
        argp.print_help()
else:
    argp.print_help()
