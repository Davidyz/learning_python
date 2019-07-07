import Array, numpy, copy, turtle, time, multiprocessing
index = [0, 0]

def _is_complete(sudoku):
    '''
    Check whether a sudoku is completely filled in.
    '''
    for i in sudoku:
        if 0 in i:
            return False
    return True

def _check(array):
    '''
    Check whether the array is a valid one in a sudoku.
    '''
    temp = copy.deepcopy(array)
    temp = Array.clear_item(temp, 0)
    return len(temp) == len(set(temp))

def add_index(index):
    '''
    Return the next index in sudoku.
    '''
    if index == [8,8]:
        return None
    elif index[1] < 8:
        return [index[0], index[1] + 1]
    elif index[1] == 8:
        return [index[0] + 1, 0]

def sub_index(index):
    '''
    Return the last index in sudoku.
    '''
    if index[1] == 0:
        return [index[0] - 1, 8]
    elif index[1] > 0:
        return [index[0], index[1] - 1]

def pprint(sudoku):
    '''
    Print a Sudoku puzzle that is defined as a list with 9 items such that every item represent one of the 9 rows.
    '''
    print("+-------+-------+-------+")
    for i in range(9):
        print("| {} {} {} | {} {} {} | {} {} {} |".format(*sudoku[i]).replace("0"," "))
        if (i+1) % 3 == 0:
            print("+-------+-------+-------+")

def gen_blocks(sudoku):
    '''
    Return blocks in a sudoku.
    '''
    blocks = list([] for i in range(9))
    for i in range(9):
        row = i // 3
        for j in range(9):
            column = j // 3
            blocks[row*3+column].append(sudoku[i][j])
    return blocks

def check_sudoku(sudoku):
    '''
    Check the validity of a sudoku.
    '''
    # check rows
    for i in sudoku:
        if not _check(i):
            return False

    # check columns
    for column in range(len(sudoku)):
        array = []
        
        for row in range(len(sudoku)):
            array.append(sudoku[row][column])
        if not _check(array):
            return False

    # check blocks
    blocks = gen_blocks(sudoku)
    for i in blocks:
        if not _check(i):
            return False

    return True
            
def __enter():
    '''
    Enter a sudoku from console.
    '''
    sudoku = []
    for i in range(9):
        char = input("Enter the {}th row (all-together, eg: 123456789): ".format(str(i + 1)))
        
        sudoku.append(list(int(j) for j in char))
    return sudoku

def first_empty(sudoku):
    '''
    Return the index of the first empty cell in a sudoku.
    '''
    index = [0, 0]
    while index != None:
        if sudoku[index[0]][index[1]] == 0:
            return index
        index = add_index(index)

    return index

def draw(sudoku):
    '''
    Draw a sudoku puzzle with turtle.
    '''
    window = turtle.Screen()
    drawer = turtle.Turtle()
    window.tracer(0, 0)
    drawer.penup()
    drawer.speed(0)
    drawer.pensize(5)
    drawer.goto(-180, 180)
    drawer.setheading(0)
    drawer.pendown()
    drawer.hideturtle()

    for i in range(4):
        drawer.forward(360)
        drawer.right(90)
    
    for i in range(1, 9):
        drawer.penup()
        drawer.goto(-180, 180 - i * 40)
        drawer.setheading(0)
        if i % 3 == 0:
            drawer.pensize(3)
        else:
            drawer.pensize(1)
        drawer.pendown()
        drawer.forward(360)
        drawer.penup()
    
        drawer.goto(-180 + i * 40, 180)
        drawer.setheading(270)
        drawer.pendown()
        if i % 3 == 0:
            drawer.pensize(3)
        else:
            drawer.pensize(1)
        drawer.pendown()
        drawer.forward(360)
        drawer.penup()
    
    drawer.setheading(0)
    for i in range(9):
        drawer.goto(-165, 150 - 40 * i)
        for j in sudoku[i]:
            drawer.write(str(j).replace('0', ' '), font=('Arial', 15, 'normal'))
            drawer.forward(40)
    if (not _is_complete(sudoku)) and check_sudoku(sudoku):
        window.reset()

def count_empty(sudoku):
    '''
    Return the number of empty cells in a sudoku puzzle.
    '''
    counter = 0
    for i in sudoku:
        for j in i:
            if j == 0:
                counter += 1

    return counter
    
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

def DFS_solve(sudoku, visualise=False):
    stack = [sudoku]

    while stack:
        candidate = stack.pop()

        if _is_complete(candidate):
            if check_sudoku(candidate):
                return candidate
            else:
                continue

        index = first_empty(candidate)
        for i in range(1, 10):
            candidate[index[0]][index[1]] = i
            if check_sudoku(candidate):
                stack.append(copy.deepcopy(candidate))
                if visualise:
                    draw(candidate)
    return None

def BFS_solve(sudoku, visualise=False):
    q = [sudoku]

    while q:
        candidate = q.pop(0)
    
        if _is_complete(candidate):
            if check_sudoku(candidate):
                return candidate
            else:
                continue

        index = first_empty(candidate)
        for i in range(1, 10):
            candidate[index[0]][index[1]] = i
            if check_sudoku(candidate):
                q.append(copy.deepcopy(candidate))
                if visualise:
                    draw(candidate)
    return None

def batch_solve(list_of_sudoku, algo=BFS_solve, visualise=False, cores=max(multiprocessing.cpu_count() // 2, 1), *args):
    if cores > multiprocessing.cpu_count():
        cores = multiprocessing.cpu_count()
        print('Processes exceeded the number of cores you have. Using the total number of cores for the number of processes.')
    
    pool = multiprocessing.Pool(processes=cores)
    result = pool.starmap_async(algo, tuple((i, visualise) for i in list_of_sudoku)).get()
    return result
                    
def timer(function, *args):
    start = time.time()
    output = function(*args)
    end = time.time()
    return end - start, output

def load_sudoku(path='puzzles.txt'):
    fin = open(path, 'r')
    puzzles = fin.readlines()
    fin.close()
    puzzles = Array.clear_item(puzzles, '\n')
    for i in range(len(puzzles)):
        puzzles[i] = eval(puzzles[i])
        puzzles[i] = (puzzles[i][:9], puzzles[i][9])
    return puzzles

def dump_sudoku(array, path='puzzles.txt'):
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
        puzzle = __enter()
        puzzle.append(input("What's the difficulty of the puzzle: "))
        puzzles.append(puzzle)
        stop = bool(finished[input('Have you finished?(Y/n) ').lower()])

    return puzzles

if __name__ == '__main__':
    puzzle = __enter()
    pprint(puzzle)
    time_spent, result = timer(BFS_solve, puzzle)
    pprint(result)
    print('Solved in {}s.'.format(time_spent))
