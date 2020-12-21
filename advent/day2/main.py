import time
def decode(string):
    rule = string.split(": ")[0]
    passwd = string.split(": ")[1]
    char = rule.split(" ")[1]
    lower = rule.split(" ")[0].split("-")[0]
    upper = rule.split(" ")[0].split("-")[1]
    return passwd, char, (int(lower), int(upper))

def check1(passwd, char, lower, upper):
    occurence = passwd.count(char)
    return lower <= occurence <= upper

def check2(passwd, char, lower, upper):
    if len(passwd) < upper:
        return False
    return int(passwd[lower - 1] == char) + int(passwd[upper - 1] == char) == 1

start_time = time.time()
fin = open("passwords.txt")
count1 = 0
count2 = 0

for i in fin.readlines():
    passwd, char, limits = decode(i)
    count1 += int(check1(passwd, char, limits[0], limits[1]))
    count2 += int(check2(passwd, char, limits[0], limits[1]))

print("part1: {}\npart2: {}\ntime: {}".format(count1, count2, round(time.time() - start_time, 10)))
