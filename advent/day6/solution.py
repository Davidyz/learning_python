content = []
with open('input.txt') as fin:
    for i in fin.readlines():
        if len(i) == 1:
            content.append(i)
            continue

        content.append(i.replace('\n', ''))

content1 = [set([j for j in i]) for i in ''.join(content).split('\n')]

count2 = 0
for i in range(len(content)):
    if content[i] != '\n':
        content[i] += '.'

for i in ''.join(content).split('\n'):
    grouplen = i.count('.')
    i = ''.join(i)
    choices = set()

    for j in i:
        if i.count(j) == grouplen and (not j == '.'):
            choices.add(j)
    print(choices)
    count2 += len(choices)

print(sum([len(i) for i in content1]), count2)
