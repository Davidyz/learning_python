import Sudoku, csv, multiprocessing, copy, time
import pysnooper

puzzles = Sudoku.load_sudoku('puzzles.txt')
size = len(puzzles)
headers = ['number_of_blank', 'dificulty', 'DFS_time_spent', 'BFS_time_spent', 'elimination_time_spent', 'DFS_weight', 'BFS_weight']

difficulty = {'easy':1,
              'medium':2,
              'hard':3,
              'extreme':4}

data = []
for i in puzzles:
    data.append([Sudoku.count_empty(i[0]), difficulty[i[1]], 0, 0, 0, 0, 0])

start = time.time()
pool = multiprocessing.Pool(4)
DFS_times = pool.starmap_async(Sudoku.timer, ((Sudoku.DFS_solve, Sudoku.Board(i[0])) for i in copy.deepcopy(puzzles)))
BFS_times = pool.starmap_async(Sudoku.timer, ((Sudoku.BFS_solve, Sudoku.Board(i[0])) for i in copy.deepcopy(puzzles)))
Eli_times = pool.starmap_async(Sudoku.timer, ((Sudoku.elimination_solve, i[0]) for i in copy.deepcopy(puzzles)))
DFS_weight_times = pool.starmap_async(Sudoku.timer, ((Sudoku.DFS_weight, Sudoku.Board(i[0])) for i in copy.deepcopy(puzzles)))
BFS_weight_times = pool.starmap_async(Sudoku.timer, ((Sudoku.BFS_weight, Sudoku.Board(i[0])) for i in copy.deepcopy(puzzles)))

pool.close()
pool.join()

DFS_times = [i[0] for i in DFS_times.get()] 
BFS_times = [i[0] for i in BFS_times.get()]
Eli_times = [i[0] for i in Eli_times.get()]
DFS_weight_times = [i[0] for i in DFS_weight_times.get()]
BFS_weight_times = [i[0] for i in BFS_weight_times.get()]

for i in range(size):
    data[i][2] = DFS_times[i]
    data[i][3] = BFS_times[i]
    data[i][4] = Eli_times[i]
    data[i][5] = DFS_weight_times[i]
    data[i][6] = BFS_weight_times[i]

with open('VA/data.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(data)
    f.close()

end = time.time()
print('Finished in {} seconds.'.format(str(round(end-start, 4))))
