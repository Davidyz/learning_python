#!/usr/bin/python3
#coding=utf-8
import os
path = '/mnt/c/Users/30813/Music/Eagles'
files = []
types = ['flac', 'wav', 'ape', 'mp3', 'm4a']
artist = path.split('/')[-1]
for i in os.listdir(path):
    if i.split('.')[-1] in types:
        files.append(i)

command = '''tracktag "{path}/{song}" --name={title} --artist={artist}''' #--album={album}'''
for i in files:
    if i.split('.')[-1] in types:
        print(i)
        os.system(command.format(path=path,
                                 song=i,
                                 title=str(i.split('.')[:-1])[1:-1],
                                 artist=artist,
                                 album=path.split('/')[-1]))
