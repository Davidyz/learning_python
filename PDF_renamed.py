#!/usr/bin/python3
'''
Automatically rename .pdf homeworks into a certain format.
'''
import os, time, UnixIO, hashlib
path = '/home/davidyz/SFTP/2020 Online Edu/Further maths/Assignment/'

def get_md5(file_path):
    f = open(file_path,'rb')  
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5

while True:
    files = [i for i in UnixIO.listdir(path) if ('done' in i or 'compressed' in i) and (not 'Mechanics' in i)]
    for i in files:
        if '\xa0' in i:
            UnixIO.mv(i, i.replace('\xa0', ' '))
            files.remove(i)
            files.append(i.replace('\xa0', ' '))
    
    for i in files:
        new = i.replace(i.split('/')[-1], "A2-C David {subject} {index}.pdf".format(subject = i.split('/')[-2][:4].upper(),
                                                                                    index = i.split('/')[-1].split(' ')[1]))
        if os.path.isfile(new) and (get_md5(i) == get_md5(new)):
            continue
        UnixIO.cp(i, new)
    time.sleep(10)