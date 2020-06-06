import UnixIO, os, time

path = '/home/davidyz/SFTP/Videos/'
files = [i for i in os.listdir(path) if (('mkv' in i) or ('mp4' in i)) and (not 'remastered' in i)]

