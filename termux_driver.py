import sys, os
sys.path.append('module')
print(sys.argv)

command = ' '.join(sys.argv[1:])
os.system(command)
