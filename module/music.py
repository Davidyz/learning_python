#coding=utf-8
'''
This is a personal module for music tagging and .lrc file processing. Mutagen integrated.
'''

import os, mutagen, mutagen.flac, json, UnixIO
from mutagen.easyid3 import EasyID3

lossless = ['ape', 'wav', 'flac', 'dsd', 'dsf', 'dff']
skip_tagging = ['dsd', 'dsf', 'dff']

def is_music(name):
    return (name.split('.')[-1] in ('mp3', 'aac', 'm4a', 'flac', 'ape', 'wav', 'dsd', 'dsf', 'dff')) and os.path.isfile(name)

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

            if not self.form in ('mp3', 'flac') or self.__strict_mod:
                self.parse_path()
            else:
                if not self.parse_tag():
                    self.parse_path()

            if 'cover.jpg' in os.listdir(os.path.sep.join(path.split('/')[:-1])):
                self.album_art = path.replace(self.__path[-1], 'cover.jpg')
            else:
                self.album_art = None
        else:
            raise InputError('\nInvalid path: {}.\nIt is a directory or is not a recognised music file.'.format(path))
    
    def __str__(self):
        return os.path.sep.join(self.__path)

    def __repr__(self):
        return str(self)

    def __getitem__(self, key):
        return self.info[key]

    def __setitem__(self, key, value):
        self.info[key] = value

    def __iter__(self):
        for i in self.info:
            yield i

    def __dict__(self):
        return self.info

    def parse_path(self):
        self.info = {'title':''.join(self.__rawinfo[-1].split('.')[:-1])}
        if len(self.__rawinfo) >= 2:
            self.info['artist'] = self.__rawinfo[0]
        if len(self.__rawinfo) >= 3:
            self.info['album'] = self.__rawinfo[1]
       
        if self.__strict_mod:
            for i in ['artist', 'album']:
                if not (i in self.info):
                    self.info[i] = ""
        return self.info

    def parse_tag(self):
        if self.form == 'flac':
            try:
                song = mutagen.flac.FLAC(self.path())
                self.info = dict(song)
            except mutagen.flac.FLACNoHeaderError:
                print('Unsupported file!')
                return False
            return self.info
        elif self.form == 'mp3':
            pass
        return False

    def load(self, path = None):
        '''
        Load a json file for the album.
        '''
        if path == None:
            path = os.path.sep.join(self.__path[:-1])

        if 'meta.json' in os.listdir(path):
            with open(path + '/meta.json') as fin:
                data = json.load(fin)
                self.info = data
                fin.close()

        elif os.path.isdir(path) and 'meta.json' in os.listdir(path):
            path = os.path.sep.join((path, 'meta.json'))
            data = self.load(path)
            self.info = data

        return data

    def dump(self, path = None):
        '''
        Dump the information of the album into a json file.
        '''
        if path == None:
            path = os.path.sep.join(self.__path[:-1] + ['meta.json'])
        with open(path, 'w') as fin:
            json.dump(self.info, fin)
            fin.close()

    def set_tag(self):
        if self.form == 'flac':
            try:
                song = mutagen.flac.FLAC(os.path.sep.join(self.__path))
                for i in self.info:
                    song[i] = self.info[i]
                if self.album_art:
                    song.add_picture(self.album_art)
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

    def path(self):
        return os.path.sep.join(self.__path)

    def format(self, target=None, form=None, bitrate=320, overwrite=True):
        if target == None:
            raise ValueError("No target directory is passed.") 
        if form == None:
            form = self.form
        
        original_path = os.path.sep.join(self.__path)
        if os.path.isdir(target):
            target_file = os.path.sep.join([target, self.__path[-1]]).replace(self.form, form)
        elif os.path.isfile(target) :
            if overwrite:
                target_file = target
            else:
                raise IOError("Target already exists.")
        
        form = target_file.split('.')[-1]
        codec = {'flac':'',
                 'aac':' -c:a libfdk_aac ',
                 'mp3':' -c:a libmp3lame '}

        command = 'ffmpeg -i "{}" -q 0 -map_metadata 0 "{}" -y -loglevel quiet'.format(original_path, target_file)
        if form in codec:  
            command += codec[form]
        if isinstance(bitrate, int) and form=='mp3':
            command += ' -b:a {}k '.format(str(bitrate))
        os.system(command)

class Lyric(Music):
    def __init__(self, path, strict_mod):
        Music.__init__(self, path, strict_mod)
        self.lyric = {}

    def append(self, time, line):
        """
        Add a new line to the lyric (cached).
        """
        time = ('[' + time + ']').split(':')
        for i in time:
            if len(i) < 2:
                i = '0' + i
            
        self.lyric[':'.join(time)] = line
        copy = {}
        for i in sorted(self.lyric.keys()):
            copy[i] = self.lyric[i]
        self.lyric = copy
    
    def pprint(self):
        for i in self.lyric:
            print(i, self.lyric[i])

    def loadLRC(self, path=None):
        """
        Read an existing lrc file and store the infomation in a dict().
        """
        if os.path.isfile(self.path().replace(self.form, 'lrc')) and path == None:
            path = self.path().replace(self.form, 'lrc')

        elif not os.path.isfile(path):
            return

        with open(path) as fin:
            content = fin.readlines()
            for i in content:
                i = i.replace('\n', '')
                if i == '':
                    continue

                try:
                    key = i[:i.index(']') + 1]
                    value = i[i.index(']') + 1:]
                except ValueError:
                    key = i
                    value = ''
                
                if 'al:' in key:
                    self.info['album'] = key[key.index(':') + 1:-1]
                elif 'ar:' in key:
                    self.info['artist'] = key[key.index(':') + 1:-1]

                if value == '':
                    try:
                        print(key)
                        int(key[1])
                    except ValueError:
                        continue

                self.lyric[key] = value

    def dumpLRC(self, path = None):
        """
        Write the cached lyric information into a lrc file. Overwrite if existing.
        """
        if path == None:
            path = self.path().replace(self.form, 'lrc')

        with open(path, 'w') as fin:
            for i in self.info:
                if self.info[i] != '':
                    fin.write('[{}:{}]\n'.format(i[:2], self.info[i]))
            
            fin.write('[by:Davidyz]\n')

            for i in self.lyric:
                fin.write(i + self.lyric[i] + '\n')
            fin.close()
    
    def modify(self, time, line):
        """
        Modify a specific line in the lyrics.
        """
        self.lyric['[' + time + ']'] = line
        
    def remove(self, time):
        """
        Remove a specific line in the lyrics.
        """
        key = time
        if not '[' in time:
            key = '[' + time + ']'

        if key in self.lyric:
            del self.lyric[key]

def format(song):
    if song.form in ('wav', 'ape'):
        new_path = '.'.join(song.split('.')[:-1] + ['flac'])
        os.system('ffmpeg -i {} -q 0 {}'.format(song, new_path))
        os.system('rm ' + song)
    else:
        pass
