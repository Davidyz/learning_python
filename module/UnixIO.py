import os
import subprocess
import json
from typing import Iterator, List, Dict


def listdir(path: str = ".") -> Iterator[str]:
    stack = [os.path.join(path, i) for i in os.listdir(path)]
    while stack:
        candidate = stack.pop(-1)
        if os.path.isfile(candidate):
            yield os.path.realpath(candidate)
        else:
            for i in os.listdir(candidate):
                stack.append(os.path.join(candidate, i))


def readfile(path: str, binary=False) -> List[str]:
    option = "r"
    if binary:
        option += "b"
    fin = open(path, option)
    content = fin.readlines()
    fin.close()
    return content


def writefile(path, content):
    fin = open(path, "w")
    if isinstance(content, str):
        fin.writelines(content)
    elif isinstance(content, list):
        fin.writelines(content)
    fin.close()


def mv(x, y):
    os.system('mv "{}" "{}"'.format(x, y))


def cp(x, y):
    os.system('cp "{}" "{}"'.format(x, y))


def rm(fin):
    os.system('rm "{}"'.format(fin))


def ffprobe(song: str) -> Dict:
    command = 'ffprobe -v quiet -hide_banner -print_format json -show_format -show_streams "{}"'.format(
        song
    )
    output = subprocess.check_output(command, shell=True)
    return json.loads(output.decode("utf-8"))
