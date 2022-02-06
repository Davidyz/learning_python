import sys, os

sys.path.append("/home/david/git/learning_python/module/")
import sort

target_dir = "/home/david/git/learning_python/wordplay/"
fin = open(sys.argv[1], "r")
wordlist = sort.quicksort(list(i[:-1] for i in fin.readlines()))
fin.close()

new_file_name = "new_{}".format(sys.argv[1].split("/")[-1])

if not new_file_name in os.listdir(target_dir):
    os.system("touch {}".format(target_dir + new_file_name))

target_file = open(target_dir + new_file_name, "w")
for i in wordlist:
    target_file.write(i + "\n")
target_file.close()
