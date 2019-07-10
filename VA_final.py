import Sudoku, csv, multiprocessing, copy
import pysnooper

puzzles = Sudoku.load_sudoku('puzzles.txt')
size = len(puzzles)
headers = ['number_of_blank', 'dificulty', 'DFS_time_spent', 'BFS_time_spent', 'elimination_time_spent']

difficulty = {'easy':1,
              'medium':2,
              'hard':3,
              'extreme':4}

data = []
for i in puzzles:
    data.append([Sudoku.blank_cells(i[0]), difficulty[i[1]], 0, 0, 0])

pool = multiprocessing.Pool(4)
DFS_times = pool.starmap_async(Sudoku.timer, ((Sudoku.DFS_solve, i[0]) for i in copy.deepcopy(puzzles)))
BFS_times = pool.starmap_async(Sudoku.timer, ((Sudoku.BFS_solve, i[0]) for i in copy.deepcopy(puzzles)))
Eli_times = pool.starmap_async(Sudoku.timer, ((Sudoku.elimination_solve, i[0]) for i in copy.deepcopy(puzzles)))

pool.close()
pool.join()

DFS_times = [i[0] for i in DFS_times.get()] 
BFS_times = [i[0] for i in BFS_times.get()]
Eli_times = [i[0] for i in Eli_times.get()]

for i in range(size):
    data[i][2] = DFS_times[i]
    data[i][3] = BFS_times[i]
    data[i][4] = Eli_times[i]

with open('data_jit.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(data)
    f.close()
