#coding=utf-8
'''
This is a personal module for music tagging (currently support ID3 tags only because it use 'audiotools', which support ID3 only, under *nix environment). Hopefully new functions can be added.
'''

import os, mutagen, mutagen.flac
from mutagen.easyid3 import EasyID3

lossless = ['ape', 'wav', 'flac', 'dsd', 'dsf', 'dff']
skip_tagging = ['dsd', 'dsf', 'dff']

def is_music(name):
    return name.split('.')[-1] in ['mp3', 'aac', 'm4a', 'flac', 'ape', 'wav', 'dsd', 'dsf', 'dff'] and os.path.isfile(name)

def all_music(array):
    for i in array:
        if not is_music(i):
            return False
    return True

class InputError(Exception):
    pass

class Music():
    '''
    The class for a music object, designed for music tagging.
    Author: Davidyz.
    '''
    def __init__(self, path, strict_mod = False):
        '''
        It is better that the path is the absolute directory.
        If strict_mod is True, the artist and album of the songs will be wiped if the song is not in a directory specifying these infomation.
        '''
        self.__lossless =  path.split('.')[-1] in lossless
        self.__strict_mod = strict_mod
        self.form = path.split('.')[-1]
        self.unsupported = False

        if is_music(path):
            self.__path = path.split(os.path.sep)
            self.__rawinfo = self.__path[self.__path.index('Music') + 1:]
            
            self.info = {'title':''.join(self.__rawinfo[-1].split('.')[:-1])}
            if len(self.__rawinfo) >= 2:
                self.info['artist'] = self.__rawinfo[0]
            if len(self.__rawinfo) >= 3:
                self.info['album'] = self.__rawinfo[1]
            
            if self.__strict_mod:
                for i in ['artist', 'album']:
                    if not (i in self.info):
                        self.info[i] = ""
            if 'cover.jpg' in os.listdir(os.path.sep.join(path.split('/')[:-1])):
                self.album_art = os.path.join(path, 'cover.jpg')

        else:
            raise InputError('\nInvalid path: {}.\nIt is a directory or is not a recognised music file.'.format(path))

    def set_tag(self):
        if self.form == 'flac':
            try:
                song = mutagen.flac.FLAC(os.path.sep.join(self.__path))
                for i in self.info:
                    song[i] = self.info[i]
                song.save()
            except mutagen.flac.FLACNoHeaderError:
                print('Unsupported file!')
                self.unsupported = True
        
        elif self.form == 'mp3':
            if self.__strict_mod == True:
                EasyID3(os.path.sep.join(self.__path)).delete()

            try:
                tag = EasyID3(os.path.sep.join(self.__path))

            except Exception:
                tag = mutagen.File(os.path.sep.join(self.__path), easy=True)
                tag.add_tags()
            
            for i in self.info:
                tag[i] = self.info[i]
            tag.save(v2_version=3)

        else:
            pass

    def is_lossless(self):
        return self.__lossless

    def info(self):
        return self.__info

    def path(self):
        return os.path.join(self.__path)

def format(song):
    if song.split('.')[-1] in ('wav', 'ape'):
        new_path = '.'.join(song.split('.')[:-1] + ['flac'])
        os.system('ffmpeg -i {} -q 0 {}'.format(song, new_path))
        os.system('rm ' + song)
    else:
        pass
