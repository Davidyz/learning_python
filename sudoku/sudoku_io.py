import Sudoku, Array

def load(path):
    fin = open(path, 'r')
    puzzles = fin.readlines()
    fin.close()
    puzzles = Array.clear_item(puzzles, '\n')
    for i in range(len(puzzles)):
        puzzles[i] = eval(puzzles[i])
    return puzzles

def dump(array, path):
    fin = open(path, 'r')
    legacy = fin.readlines()
    fin.close()
    fin = open(path, 'w')
    content = Array.clear_item(legacy + array, '\n')
    for i in content:
        fin.write(str(i) + '\n')
    fin.close()

def ask_for_puzzle():
    puzzles = []
    stop = False
    finished = {'y':True,
                'n':False,
                '':True}

    while not stop:
        puzzles.append(Sudoku._enter())
        stop = bool(finished[input('Have you finished?(Y/n) ').lower()])

    return puzzles

if __name__ == '__main__':
    import sudoku_solver
    #dump(ask_for_puzzle(), 'puzzles.txt')
    
    puzzles = load('puzzles.txt')
    for i in puzzles:
        Sudoku.pprint(i)
        time_spent, result = sudoku_solver.timer(sudoku_solver.DFS_solve, i)
        Sudoku.pprint(result)
        print(time_spent)
        print('=' * 30)
    #Sudoku.pprint(sudoku_solver.DFS_solve(puzzles))
