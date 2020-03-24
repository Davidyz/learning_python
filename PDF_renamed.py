#!/usr/bin/python3
'''
Automatically rename .pdf homeworks into a certain format.
'''
import os, time, UnixIO, hashlib, pysnooper
path = '/home/davidyz/SFTP/2020 Online Edu/Further maths/Assignment/'
subject = {'PURE':'Pure Maths', 'STAT':'Statistics'}

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

def PDF_rename(path):
    files = [i for i in UnixIO.listdir(path) if ('done' in i or 'compressed' in i) and (not 'Mechanics' in i) and (not 'sewing' in i)]
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
        print(i)
        if 'Assignment' in i.split('/')[-1]:
            UnixIO.cp(i, new)
        else:
            UnixIO.mv(i, new)

while True:
    PDF_rename(path)
    time.sleep(10)
