#coding=utf-8
'''
This is a personal module for music tagging (currently support ID3 tags only because it use 'audiotools', which support ID3 only, under *nix environment). Hopefully new functions can be added.
'''

import os

lossless = ['ape', 'wav', 'flac', 'dsd', 'dsf', 'dff']

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

        if is_music(path):
            self.__path = path.split('/')
            self.__info = self.__path[self.__path.index('Music') + 1:]
            self.title = "{}".format(''.join(self.__info[-1].split('.')[:-1]))
            
            self.command = '''tracktag "{path}" --name="{name}"'''.format(path=path,
                                                                      name=self.title)

            if len(self.__info) >= 2:
                self.artist = '''"{}"'''.format(self.__info[0])
            elif strict_mod and len(self.__info) < 2:
                self.artist = '''""'''
        
            if len(self.__info) == 3:
                self.album = '''"{}"'''.format(self.__info[1])
            elif strict_mod and len(self.__info) < 3:
                self.album = '''""'''

        else:
            raise InputError('\nInvalid path: {}.\nIt is a directory or is not a recognised music file.'.format(path))

    def set_tag(self):
        try:
            self.command += ' --artist={}'.format(self.artist)
            self.command += ' --album={}'.format(self.album)
        except AttributeError:
            pass
        os.system(self.command)

    def is_lossless(self):
        return self.__lossless
