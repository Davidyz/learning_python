import csv, math
import matplotlib.pyplot as plt
from scipy import optimize

def func(x, a, b):
    return math.e ** (a * x) + b

data = []
with open('VA/data.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i in f_csv:
        data.append(list(i))
    f.close()

blanks = [int(i[0]) for i in data]
difficulty = [int(i[1]) for i in data]
DFS_time = [math.log10(float(i[2]) + 1) for i in data]
BFS_time = [math.log10(float(i[3]) + 1) for i in data]
Eli_time = [math.log10(float(i[4]) + 1) for i in data]
DFS_weight = [math.log10(float(i[5]) + 1) for i in data]
BFS_weight = [math.log10(float(i[6]) + 1) for i in data]
x = [i * 0.05 for i in range(math.floor((min(blanks) - 3) / 0.05), math.ceil((max(blanks) + 3) / 0.05))]

# Blanks
plt.plot(blanks, DFS_time, linestyle='', marker='^', label='DFS', color='b')
arg, mat = optimize.curve_fit(func, blanks, DFS_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='b')

plt.plot(blanks, BFS_time, linestyle='', marker='h', label='BFS', color='r')
arg, mat = optimize.curve_fit(func, blanks, BFS_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='r')

plt.plot(blanks, Eli_time, linestyle='', marker='.', label='Elimination', color='k')
arg, mat = optimize.curve_fit(func, blanks, Eli_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='k')

plt.plot(blanks, DFS_weight, linestyle='', marker='v', label='DFS Weighted', color='g')
arg, mat = optimize.curve_fit(func, blanks, DFS_weight)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='g')

plt.plot(blanks, BFS_weight, linestyle='', marker='H', label='BFS Weighted', color='y')
arg, mat = optimize.curve_fit(func, blanks, BFS_weight)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='y')

plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))
plt.title('Running Time VS. Empty Cells')
plt.xlabel('Number of Empty Cells')
plt.ylabel('Log10(time spent + 1)')
plt.savefig('VA/blanks.png', dpi=720)
plt.cla()

# Difficulties
x = [i * 0.05 for i in range(math.floor(1 / 0.05), math.ceil((4 / 0.05)))]
plt.plot(difficulty, DFS_time, linestyle='', marker='^', label='DFS', color='b')
arg, mat = optimize.curve_fit(func, difficulty, DFS_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='b')

plt.plot(difficulty, BFS_time, linestyle='', marker='s', label='BFS', color='r')
arg, mat = optimize.curve_fit(func, difficulty, BFS_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='r')

plt.plot(difficulty, Eli_time, linestyle='', marker='.', label='Elimination', color='k')
arg, mat = optimize.curve_fit(func, difficulty, Eli_time)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='k')

plt.plot(difficulty, DFS_weight, linestyle='', marker='v', label='DFS Weighted', color='g')
arg, mat = optimize.curve_fit(func, difficulty, DFS_weight)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='g')

plt.plot(difficulty, BFS_weight, linestyle='', marker='H', label='BFS Weighted', color='y')
arg, mat = optimize.curve_fit(func, difficulty, BFS_weight)
y = [func(i, arg[0], arg[1]) for i in x]
plt.plot(x, y, linestyle=':', marker='', color='y')

plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))
plt.title("Running Time VS. 'Difficulty' for Humans")
plt.xlabel('Difficulty for Humans')
plt.ylabel('Log10(time spent + 1)')
plt.savefig('VA/difficulty.png', dpi=720)
