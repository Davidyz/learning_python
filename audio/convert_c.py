import os, sys

class Music():
    '''
    The class for a music object.
    '''
    def __init__(self, title, form, lossless = True, path, artist = None, album = None)
        self.title = title
        self.form = form
        self.lossless = lossless
        self.path = path
        self.artist = artist
        self.album = album

    def set_artist(self, name):
        pass

if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Missing argument! Please enter the path!')

