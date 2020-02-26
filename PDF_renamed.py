#!/usr/bin/python3
import os, time
from module import UnixIO
path = '/home/davidyz/SFTP/2020 Online Edu/Further maths/Assignment/'
while True:
    files = [i for i in UnixIO.listdir(path) if 'compressed' in i and (not 'Mechanics' in i)]
    for i in files:
        UnixIO.cp(i, "A2-C David {subject} {index}.pdf".format(subject = i.split('/')[-2][:4].upper(),
                                                               index = i.split('/'.)split(' ')[1]))
    time.sleep(10)