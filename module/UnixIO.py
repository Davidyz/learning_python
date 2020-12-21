import os
def listdir(path):
    stack = [os.path.join(path, i) for i in os.listdir(path)]
    output = []
    while stack:
        candidate = stack.pop(-1)
        if os.path.isfile(candidate):
            output.append(candidate)
        else:
            for i in os.listdir(candidate):
                stack.append(os.path.join(candidate, i))
    return sorted(output)

def readfile(path, binary=False):
    option = 'r'
    if binary:
        option += 'b'
    fin = open(path, option)
    content = fin.readlines()
    fin.close()
    return content

def writefile(path, content):
    fin = open(path, 'w')
    if isinstance(content, str):
        fin.writeline(content)
    elif isinstance(content, list):
        fin.writelines(content)
    fin.close()

def mv(x, y):
    os.system('mv "{}" "{}"'.format(x, y))

def cp(x, y):
    os.system('cp "{}" "{}"'.format(x, y))

def rm(fin):
    os.system('rm "{}"'.format(fin))
