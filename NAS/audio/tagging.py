import music, UnixIO, sys, os

def printf(song):
    info = ''
    for i in song.info:
        info += i + ': ' + song.info[i] + '; '
    print(info)

if '-s' in sys.argv:
    strict = True
    sys.argv.remove('-s')
else:
    strict = False

if len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        single = None
    elif music.is_music(sys.argv[1]):
        path = None
        single = music.Lyric(sys.argv[1], strict)

if single:
    single.set_tag()

elif path:
    for i in (j for j in UnixIO.listdir(path) if music.is_music(j)):
        song = music.Lyric(i, strict)
        printf(song)
        song.set_tag()
