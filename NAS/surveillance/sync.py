import os
import time

local_dir = "~/surveillance"
remote_dirs = {"": 15}  # key pairs: directory (str) : days saved (int)


def get_duration(clip):  # Get the duration of a clip.
    import cv2

    video = cv2.VideoCapture(clip)
    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    return duration


for clip in os.listdir(local_dir):  # Upload new clips.
    for drive in remote_dirs:
        if not clip in os.listdir(drive):
            os.system(
                'cp "{source}" "{target}"'.format(
                    source=os.path.join(local_dir, clip), target=drive
                )
            )

for drive in remote_dirs:  # Clear remote clips
    for i in os.listdir(drive):
        if (
            time.time() - os.path.getmtime(os.path.join(drive, i))
            >= remote_dirs[drive] * 24 * 60 * 60
        ):
            os.system('rm "{}"'.format(os.path.join(drive, i)))
