import os
import time
from datetime import date
output_dir = '~/surveillance/'
# Check the existence of the recording directory.
if not os.path.isdir(output_dir):
    os.system('mkdir ' + output_dir)

days_saved = 7  # The number of days that a clip will be saved locally.
IPcam_url = ''  # The url of the IP camera.
command = '''ffmpeg -i {camera} -c:v copy -r 30 -t 3600 -map 0 {file_name}.mkv'''.format(camera=IPcam_url,
                                                                                         file_name=time.ctime()[4:].replace(' ', '_') + '.mkv')

while True:
    os.system(command)
    old_clip = [i for i in os.listdir(output_dir) if time.time(
    ) - os.path.getmtime(i) >= days_saved * 24 * 60 * 60]
    for i in old_clip:
        os.system('rm ' + os.path.join(output_dir, i))
