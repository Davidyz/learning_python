#!/usr/bin/python3
#coding=utf-8
import os, sys
command = '''ffmpeg -i "{origin}" "{output}"'''
to_be_converted = ['wav', 'ape']
music_files = ['wav', 'ape', 'flac', 'mp3', 'm4a', 'dsf', 'dff']
covers = ['cover.jpg', 'cover.png']
singers_and_albums = {}
all_songs = []

def is_song(item):
    if item.split('.')[-1] in music_files:
        return True
    return False

def set_singers():
    '''
    Generate a dict where the keys are the names of the artists.
    '''
    for i in os.listdir(rootdir):
        if os.path.isdir(rootdir + i):
            singers_and_albums[i] = []

def set_albums():
    '''
    Append the albums of each artist into the dict.
    '''
    for i in singers_and_albums:    # iter through each singer
        for j in os.listdir(rootdir + i):   # iter through each album of the singer
            if os.path.isdir(rootdir + i + '/' + j):
                singers_and_albums[i].append(j)

def title(song):
    '''
    Return the title of the song based on the file name.
    '''
    song = song.split('.')[:-1]
    name = ''
    for i in song:
        name += i
    return name

def gen_song_list():
    '''
    Generate a list of the abs directory of the songs.
    '''
    # First step (no specified singer)
    for i in os.listdir(rootdir):
        if is_song(i):
            all_songs.append(rootdir + i)

    # Second step (specified singer, non-specified album)
    for i in singers_and_albums:    # iter through each singer
        for j in os.listdir(rootdir + i):   # iter through each item
            if is_song(j):
                all_songs.append(rootdir + i + '/' + j)

    # Third step (specified singer and specified album)
    for singer in singers_and_albums:    # iter through each singer
        for album in singers_and_albums[singer]:    # iter through each album of the singer
            for item in os.listdir(rootdir + singer + '/' + album):    # iter through each item in the album
                if is_song(item):
                    all_songs.append(rootdir + singer + '/' + album + '/' + item)

def convert_into_flac(list_of_songs):
    for i in range(len(list_of_songs)):
        if list_of_songs[i].split('.')[-1] in to_be_converted:
            name = title(list_of_songs[i])
            print('Converting {}'.format(name))
            os.system(command.format(origin=list_of_songs[i], output=name + '.flac'))
            #list_of_songs.pop(i)
            os.system('rm {}'.format(list_of_songs.pop(i)))
            list_of_songs.insert(i, name + '.flac')

def add_tags(list_of_songs):
    '''
    Add tags for songs.
    '''
    for i in list_of_songs:
        info = i.split('/')
        name = title(info[-1])
        if len(info) == 9:
            artist = info[6]
            album = info[7]
        if len(info) == 8:
            artist = info[6]
            album = ""
        if len(info) == 7:
            artist, album = "", ""
        command = '''tracktag "{song}" --name="{name}" --artist="{artist}" --album="{album}"'''.format(song=i,
                                                                                                       name=title(i.split('/')[-1]),
                                                                                                       artist=artist,
                                                                                                       album=album)
        print(name)
        os.system(command)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        rootdir = sys.argv[1]
    
    else:
        print('Fail to pass the root directory of your music library as an argument!\nProgress may fail!')
        rootdir = '/mnt/c/Users/30813/Music/'
    
    set_singers()
    set_albums()
    gen_song_list()
    convert_into_flac(all_songs)
    add_tags(all_songs)
