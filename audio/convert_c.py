import os, sys

class Music():
    '''
    The class for a music object.
    '''
    def __init__(self, title, form, lossless = True, is_dsd = False, path, artist = None, album = None)
        self.title = title
        self.form = form
        self.lossless = lossless
        self.dsd = is_dsd
        self.path = path
        self.artist = artist
        self.album = album
        self.tagging = '''tracktag {directory} '''
        self.convert = '''ffmpeg -i {} {}'''

    def set_artist(self):
        self.tagging += '''--artist="{}" '''.format(self.artist)

    def set_album(self):
        self.tagging += '''--album="{}" '''.format(self.album)

    def add_tag(self):
        os.system(self.tagging.format(directory = self.path)

    def convert(self):
        if self.lossless and not self.is_dsd:
            mother_dir = ''.join(self.path.split('/')[:-1])
            os.system(self.convert.format("""{}""".format(self.path), '"""' + mother_dir + self.title + '.flac"""'))
            os.system('''rm {}'''.format(self.path))

if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Missing argument! Please enter the path!')

