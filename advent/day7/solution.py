bags = set()
contains = {}
true = set()
false = set()


def get_bags(string):
    if string == "no other bag":
        return []

    stuffing = string.split(",")
    bags = []
    for i in stuffing:
        info = [j for j in i.split(" ") if not j == ""]
        try:
            number = int(info[0])
            name = " ".join(info[1:])
            bags += [name] * number
        except:
            print(info)

    return bags


def search_1(bag):
    if bag in true:
        return True
    elif bag in false:
        return False

    if "shiny gold bag" in contains[bag]:
        true.add(bag)
        return True
    if not contains[bag]:
        false.add(bag)
        return False

    for i in contains[bag]:
        if search_1(i):
            true.add(i)
            return True
    false.add(bag)
    return False


def search_2(bag):
    count = 0
    if contains[bag]:
        count += len(contains[bag])
        count += sum([search_2(i) for i in contains[bag]])
        return count
    else:
        return 0


with open("input.txt") as fin:
    content = [i.replace("\n", "") for i in fin.readlines()]

for i in range(len(content)):
    content[i] = content[i].split(" contain ")
    bags.add(content[i][0])
    contains[content[i][0]] = get_bags(content[i][1])

count1 = 0
for i in bags:
    count1 += search_1(i)

print(count1, search_2("shiny gold bag"))
