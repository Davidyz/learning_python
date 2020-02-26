#!/usr/bin/python3
import os, time, UnixIO
path = '/home/davidyz/SFTP/2020 Online Edu/Further maths/Assignment/'
while True:
    files = [i for i in UnixIO.listdir(path) if 'compressed' in i and (not 'Mechanics' in i)]
    for i in files:
        if '\xa0' in i:
            UnixIO.mv(i, i.replace('\xa0', ' '))
            files.remove(i)
            files.append(i.replace('\xa0', ' '))
    
    for i in files:
        new = i.replace(i.split('/')[-1], "A2-C David {subject} {index}.pdf".format(subject = i.split('/')[-2][:4].upper(),
                                                                                    index = i.split('/')[-1].split(' ')[1]))
        if os.path.isfile(new):
            continue
        UnixIO.cp(i, new)
    time.sleep(10)