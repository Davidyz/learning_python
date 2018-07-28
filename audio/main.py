#coding=utf-8
import os, sys
sys.path.append('/home/david/git/learning_python/module/')
from music import *

try:
    music_rootdir = sys.argv[1]
    if os.path.isdir(music_rootdir):
        pass
    else:
        raise IOError('Not a valid directory: {}'.format(sys.argv[1]))
except IndexError:
    print('Please specify a directory!')
    exit()

list_of_paths = []
list_of_music_objects = []

def generate_song_list(rootdir):
    complete = False
    l = [os.path.join(rootdir, i) for i in os.listdir(rootdir)]
    while not complete:
        complete = True
        for i in l:
            if is_music(i):
                pass
            if os.path.isdir(i):
                l += list(os.path.join(i, j) for j in os.listdir(i) if (is_music(os.path.join(i, j)) or os.path.isdir(os.path.join(i, j))))
                l.remove(i)
                complete = False
    return l

for i in generate_song_list(music_rootdir):
    print(i)
    Music(i).set_tag()
