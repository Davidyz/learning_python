#coding=utf-8
import os, sys, music

mode = 0 # 0 for single, 1 for batch.

def printf(array):
    for i in array:
        print(i, end=' ')
    print('\n')

def generate_song_list(rootdir):
    """
    For a directory of music files, return the list of song files in the provided directory and all of its subdir.
    """
    complete = False
    l = [os.path.join(rootdir, i) for i in os.listdir(rootdir)]
    while not complete:
        complete = True
        for i in l:
            if music.is_music(i):
                pass
            if os.path.isdir(i):
                l += list(os.path.join(i, j) for j in os.listdir(i) if (music.is_music(os.path.join(i, j)) or os.path.isdir(os.path.join(i, j))))
                l.remove(i)
                complete = False
    for i in l:
        if not music.is_music(i):
            l.remove(i)
    return l

def single(strict = False):
    """
    For a single audio file.
    """
    mapping = {'-artist':'artist',
               '-album':'album'}
    if not music.is_music(sys.argv[1]):             # Check the file type before the operation.
        print('This is not a valid music file!')
        exit()

    song = music.Music(sys.argv[1], strict)
    
    if '-artist' in sys.argv:
        try:
            song.artist = sys.argv[sys.argv.index('-artist') + 1]
        except IndexError:
            print('Missing Argument(s)!')
    else:
        song.artist = ''

    if '-album' in sys.argv:
        try:
            song.album = sys.argv[sys.argv.index('-album') + 1]
        except IndexError:
            print('Missing argument(s)!')
    else:
        song.album = ''

    song.set_tag()
    print(song.info())

def main():
    if '-s' in sys.argv:
        strict = True
        sys.argv.remove('-s')

    else:
        strict = False

    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        mode = 1
    elif len(sys.argv) > 2:
        mode = 0
    else:
        print('Invalid input!')
        exit()

    if mode == 1:
        song_list = generate_song_list(sys.argv[1])
        for i in song_list:
            song = music.Music(i, strict)
            printf(song.info())
            song.set_tag()
    
    elif mode == 0:
        single(strict)

if __name__ == '__main__':
    main()
