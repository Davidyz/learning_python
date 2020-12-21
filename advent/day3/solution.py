from functools import reduce
fin = open('maze.txt')
content = [i.replace("\n", '') for i in fin.readlines()]

def travel(x_step, y_step):
    x = 0
    y = 0
    count = 0
    while x < len(content[0]) and y < len(content):
        count += int(content[y][x] == "#")
        x = (x + x_step) % len(content[0])
        y += y_step
    return count

steps = [[1,1], [3,1], [5,1], [7,1], [1,2]]
for i in steps:
    i.append(travel(i[0], i[1]))

print(reduce(lambda x, y: x * y, [i[2] for i in steps]))
