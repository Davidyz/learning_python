import csv, math
import matplotlib.pyplot as plt
from scipy import optimize

def f(x, a, b):
    return math.e ** (a * x) + b

data = []
with open('data_jit.csv', 'r') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for i in f_csv:
        data.append(list(i))
    f.close()

header = {'number_of_blank':0,
          'difficulty':1,
          'DFS_time_spent':2,
          'BFS_time_spent':3}

blanks = [int(i[0]) for i in data]
difficulty = [int(i[1]) for i in data]
DFS_time = [math.log10(float(i[2]) + 1) for i in data]
BFS_time = [math.log10(float(i[3]) + 1) for i in data]
Eli_time = [math.log10(float(i[4]) + 1) for i in data]

# Blanks
plt.plot(blanks, DFS_time, linestyle='', marker='^', label='DFS')
plt.plot(blanks, BFS_time, linestyle='', marker='s', label='BFS')
plt.plot(blanks, Eli_time, linestyle='', marker='.', label='Elimination + DFS')
plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))
plt.xlabel('Number of Empty Cells')
plt.ylabel('Log10(time spent + 1)')
plt.savefig('blanks_jit.png', dpi=720)
plt.cla()

plt.plot(difficulty, DFS_time, linestyle='', marker='^', label='DFS')
plt.plot(difficulty, BFS_time, linestyle='', marker='s', label='BFS')
plt.plot(difficulty, Eli_time, linestyle='', marker='.', label='Elimination + DFS')
plt.legend(loc='upper left', bbox_to_anchor=(0.2, 0.95))
plt.xlabel('Difficulty for Humans')
plt.ylabel('Log10(time spent + 1)')
plt.savefig('difficulty_jit.png', dpi=1080)
