import UnixIO, os, time, cv2
import sys

args = sys.argv

old_path = args[1]
new_path = args[2]

for i in [old_path, new_path]:
    if i[-1] != "/":
        i += "/"

if old_path == new_path:
    os.system("mkdir tmp")
    for i in os.listdir(old_path):
        UnixIO.mv(i, "tmp")
    old_path = "tmp/"
    tmp = True
else:
    tmp = False

files = [i for i in UnixIO.listdir(old_path) if "mkv" in i or "mp4" in i or "m4v" in i]

for i in files:
    os.system(
        'ffmpeg -i "{source}" -c:v libx265 -c:a libfdk_aac -y -q 0 -y -x265-params lossless=1 "{target}"'.format(
            source=i,
            target=i.replace(old_path, new_path)
            .replace("264", "265")
            .replace("mkv", "mp4")
            .replace("m4v", "mp4"),
        )
    )

if tmp:
    os.system("rm -r tmp")
