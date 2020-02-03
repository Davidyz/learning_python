#!/usr/bin/python3
import music, UnixIO, sys, os, multiprocessing
arguments = sys.argv

replaced = '-r' in arguments
if replaced:
    arguments.remove('-r')

if len(arguments) == 3:
    for i in arguments[1:]:
        if (not os.path.isfile(i)) and (not os.path.isdir(i)):
            raise music.InputError('The input {} is not valid!'.format(i))

    args = {'original':arguments[1],'destination':arguments[2]}
elif len(arguments) == 2 and (os.path.isfile(arguments[1]) or os.path.isdir(arguments[1])):
    args = {'original':arguments[1],'destination':False}

songs = [music.Music(i) for i in UnixIO.listdir(args['original']) if music.is_music(i)]

def execute(song, replace, to):
    if replace:
        song.format('mp3', True)
        return
    song.format('mp3', False)
    if to:
        UnixIO.mv(song.path().replace(song.form, 'mp3'), to)

pool = multiprocessing.Pool(processes = 3)
pool.starmap_async(execute, ([i, replaced, args['destination']] for i in songs)).get()
pool.close()
pool.join()

if args['destination']:
    lyrics = (j for j in UnixIO.listdir(args['original']) if 'lrc' in j)
    for i in lyrics:
        UnixIO.mv(i, args['destination'])
