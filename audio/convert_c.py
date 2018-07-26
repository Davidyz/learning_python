import os, sys

def is_music(path):
    return path.split('.')[-1] in ['mp3', 'aac', 'flac', 'ape', 'wav', 'dsd', 'dsf', 'dff'] and os.path.isfile(path)

class InputError(Exception):
    pass

class Music():
    '''
    The class for a music object, designed for music tagging.
    Author: Davidyz.
    '''
    def __init__(self, path):
        if is_music(path):
            self.__path = path.split('/')
            self.__info = self.__path[self.__path.index('Music') + 1:]
            self.title = "{}".format(''.join(self.__info[-1].split('.')[:-1]))
        
            if len(self.__info) >= 2:
                self.artist = "{}".format(self.__info[0])
            else:
                self.artist = ""
        
            if len(self.__info) == 3:
                self.album = "{}".format(self.__info[1])
            else:
                self.album = ""

        else:
            raise InputError('\nInvalid path: {}.\nIt is a directory or is not a recognised music file.'.format(path))

    def set_tag(self):
        command = '''tracktag "{path}" --name="{name}" --artist="{artist}" --album="{album}"'''.format(path = '/'.join(self.__path),
                                                                                                       name = self.title,
                                                                                                       artist = self.artist,
                                                                                                       album = self.album)
        os.system(command)
