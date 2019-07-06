#!/usr/bin/python3.6
import Graph, Sudoku, copy

_sample = [[9,8,0,2,0,0,0,1,0],
           [0,3,6,0,8,1,0,5,0],
           [1,0,0,0,0,5,0,2,0],
           [0,0,0,5,0,0,2,0,1],
           [8,0,0,0,1,0,4,0,0],
           [0,6,0,0,2,0,9,0,0],
           [7,4,3,1,5,0,6,0,0],
           [0,2,0,8,4,0,0,0,7],
           [0,0,0,7,0,3,0,0,2]]

test = [[0,2,3,4,5,6,7,8,9],
        [4,5,6,7,8,9,1,2,3],
        [7,8,9,1,2,3,4,5,6],
        [2,3,4,5,6,7,8,9,1],
        [5,6,7,8,9,1,2,3,4],
        [8,9,1,2,3,4,5,6,7],
        [3,4,5,6,7,8,9,1,2],
        [6,7,8,9,1,2,3,4,5],
        [9,1,2,3,4,5,6,7,8]]

def enter_sudoku():
    sudoku = []
    
    for i in range(9):
        char = input("Enter the {}th row (all-together, eg: 123456789): ".format(str(i + 1)))
        if char == '':
            return _sample
        sudoku.append(list(int(j) for j in char))
    
    if len(sudoku) == 9:
        for i in sudoku:
            if len(i) != 9:
                print('Wrong Input!')
                return enter_sudoku()
        return sudoku

    print('Wrong Input!')
    return enter_sudoku()

'''
def fill(sudoku, row, column, value):
    sudoku[row][column] = value
    return sudoku
'''

def DFS_solve(sudoku, stack = []):
    if stack == []:
        stack = [sudoku]

    while stack:
        candidate = stack.pop()
        
        if Sudoku._is_complete(candidate):
            if Sudoku.check_sudoku(candidate):
                return candidate
            else:
                continue

        index = Sudoku.first_empty(candidate)
        for i in range(1, 10):
            candidate[index[0]][index[1]] = i
            if Sudoku.check_sudoku(candidate):
                stack.append(copy.deepcopy(candidate))

def BFS_solve(sudoku, q = []):
    if q == []:
        q = [sudoku]

    while q:
        candidate = q.pop(0)
    
        if Sudoku._is_complete(candidate):
            if Sudoku.check_sudoku(candidate):
                return candidate
            else:
                continue

        index = Sudoku.first_empty(candidate)
        for i in range(1, 10):
            candidate[index[0]][index[1]] = i
            if Sudoku.check_sudoku(candidate):
                q.append(copy.deepcopy(candidate))
    
if __name__ == '__main__':
    puzzle = enter_sudoku()
    import time
    
    Sudoku.pprint(puzzle)
    start = time.time()
    Sudoku.pprint(BFS_solve(puzzle))
    end = time.time()
    print('Solved in {}s.'.format(end - start))
