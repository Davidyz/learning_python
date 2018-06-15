import os
path = '/mnt/c/Users/30813/Music'
types = ['wav', 'ape']
command = '''track2track -t flac "{path}/{song}" -o "{output}"'''
for i in os.listdir(path):
    if i.split('.')[-1] in types:
        os.system(command.format(path=path,
                                 song=i,
                                 output="/mnt/c/Users/30813/Desktop/" + i))
