import music, UnixIO, sys, os

if "-s" in sys.argv:
    strict = True
    sys.argv.remove("-s")
else:
    strict = False

if len(sys.argv) == 2:
    if os.path.isdir(sys.argv[1]):
        path = sys.argv[1]
        single = False
    elif music.is_music(sys.argv[1]):
        path = None
        single = music.Lyric(sys.argv[1], strict)
else:
    sys.exit()

if single:
    single.set_tag()

elif path:
    for i in (j for j in UnixIO.listdir(path) if music.is_music(j)):
        try:
            song = music.Lyric(i, strict)
            print(song)
            song.set_tag()
        except (music.mutagen.flac.error, AttributeError) as error:
            print("Failed to convert " + str(song))
