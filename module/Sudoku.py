import Array, copy, turtle, time, multiprocessing, math
try:
    import pysnooper
except ModuleNotFoundError:
    pass

class Cell():
    def __doc__(self):
        '''
        The Cell object is defined for the individual cells in a sudoku puzzle. self.value stands for the value filled into the cell. If self.value == 0, it is an empty cell. 
        The __weight attribute is used to determine which cell to start filling.
        '''
    def __init__(self, index, value=0):
        self.__index = index
        self.value = value
        if value != 0:
            self.__weight = -1
        else:
            self.__weight = 0
    
    def __next__(self):
        if self.index == [8, 8]:
            return None
        elif self.index[1] == 8:
            return [self.index[0] + 1, 0]
        else:
            return [self.index[0], self.index[1] + 1]
    
    def __int__(self):
        return self.value
    
    def __eq__(self, other):
        if type(other) == type(self):
            return self.__weight == other.weight()
        else:
            return self.__weight == other

    def __ne__(self, other):
        if type(other) == type(self):
            return self.__weight != other.weight()
        else:
            return self.__weight != other

    def __gt__(self, other):
        if type(other) == type(self):
            return self.__weight > other.weight()
        else:
            return self.__weight > other
    
    def __lt__(self, other):
        if type(other) == type(self):
            return self.__weight < other.weight()
        else:
            return self.__weight < other

    def __ge__(self, other):
        if type(other) == type(self):
            return self.__weight >= other.weight()
        else:
            return self.__weight >= other

    def __le__(self, other):
        if type(other) == type(self):
            return self.__weight <= other.weight()
        else:
            return self.__weight <= other

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return self.value
    
    def is_empty(self):
        '''
        Return true if the cell is is_empty. Encapsulated to reduce the amount of effort needed while using.
        '''
        return self.value == 0
    
    def weight(self, w=None):
        '''
        Return or set the weight for a cell.
        '''
        if w == None:
            return self.__weight
        elif type(w) == int:
            self.__weight = w

    def get_index(self):
        '''
        Return the index of the cell.
        '''
        return self.__index

class Board():
    def __doc__(self):
        '''
        A class designed to help solve a sudoku puzzle.
        '''
    def __init__(self, data = [[0 for i in range(9)] for i in range(9)]):
        self.size = len(data)

        for i in range(9):
            for j in range(9):
                data[i][j] = Cell([i, j], data[i][j])
        self.__data = data
        
        self.cells = []
        for i in self.__data:
            for j in i:
                self.cells.append(j)
    
    def set_value(self, index, i):
        '''
        Set value i to the cell with given index in the board.
        '''
        self.__data[index[0]][index[1]].value = i

    def first_empty(self):
        '''
        Return the index of the first empty cell in the board.
        Return None if all of them are filled.
        '''
        for i in self.__data:
            for j in i:
                if j.value == 0:
                    return j
        return None

    def is_complete(self):
        '''
        Return true if there are no empty cells in the board.
        '''
        for i in self.cells:
            if i.value == 0:
                return False
        return True

    def gen_block(self):
        '''
        Return a list of blocks in which each block is stored as a sub-list.
        '''
        blocks = [[] for i in range(9)]
        for i in self.cells:
            row, column = i.get_index()
            blocks[row // 3 * 3 + column // 3].append(i)
        return blocks

    def validate(self):
        '''
        Check whether the sudoku is correctly filled, no matter it is fully filled or not.
        '''
        # check rows:
        for i in self.__data:
            occured = []
            for j in i:
                if (j.value != 0) and (not (j.value in occured)):
                    occured.append(j.value)
                elif j.value in occured:
                    return False

        # check columns:
        for column in range(9):
            c = []
            occured = []
            for row in range(9):
                c.append(self.__data[row][column])
            for i in c:
                if (i.value != 0) and (not (i.value in occured)):
                    occured.append(i.value)
                elif i.value in occured:
                    return False

        for i in self.gen_block():
            occured = []
            for j in i:
                if (j.value != 0) and (not (j.value in occured)):
                    occured.append(j.value)
                elif j.value in occured:
                    return False
        return True

    def gen_weight(self):
        '''
        Assign the weights for each cell.
        '''
        for i in self.cells:
            if i.value != 0:
                i.__weight = -1
                continue
            index = i.get_index()
            occured = []
            for j in self.__data[index[0]]:
                if (not j.value in occured) and (j.value != 0):
                    occured.append(j.value)

            for j in [self.__data[k][index[1]] for k in range(9)]:
                if (not (j.value in occured)) and (j.value != 0):
                    occured.append(j.value)

            for j in self.gen_block()[index[0] // 3 * 3 + index[1] // 3]:
                if (not (j.value in occured)) and (j.value != 0):
                    occured.append(j.value)
            i.weight(len(set(occured)))

    def max_weight(self):
        '''
        Return the cell with the highest weight.
        '''
        highest = self.cells[0]
        for i in self.cells[1:]:
            if i.weight() > highest.weight():
                highest = i
        return highest
    
    def pprint(self):
        '''
        Print the sudoku nicely.
        '''
        print("+-------+-------+-------+")
        for i in range(9):
            print("| {} {} {} | {} {} {} | {} {} {} |".format(*[str(j.value) for j in self.__data[i]]).replace("0"," "))
            if (i + 1) % 3 == 0:
                print("+-------+-------+-------+")
    
    def draw(self):
        '''
        Draw a sudoku puzzle with turtle.
        '''
        window = turtle.Screen()
        window.setup(400, 400)
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
            for j in self.__data[i]:
                drawer.write(str(j).replace('0', ' '), font=('Arial', 15, 'normal'))
                drawer.forward(40)
        if (not self.is_complete()) and self.validate():
            window.reset()
    
    def row(self, cell):
        return self.__data[cell.get_index()[0]]

    def column(self, cell):
        return [self.__data[i][cell.get_index()[1]] for i in range(9)]

    def block(self, cell):
        return self.gen_block()[cell.get_index()[0] // 3 * 3 + cell.get_index()[1] // 3]

    def count_empty(self):
        count = 0
        for i in self.__data:
            for j in i:
                count += int(j == 0)
        return count

def timer(function, *args):
    '''
    Measure the running time required for an operation.
    Output: time, returned value of the operation.
    '''
    start = time.time()
    result = function(*args)
    end = time.time()
    return end - start, result
            
def __enter():
    '''
    Enter a sudoku from console.
    '''
    sudoku = []
    for i in range(9):
        char = input("Enter the {}th row (all-together, eg: 123456789): ".format(str(i + 1)))
        
        sudoku.append(list(int(j) for j in char))
    return sudoku

def enter_sudoku():
    '''
    Enter a single sudoku from the console.
    '''
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
    '''
    Use DFS algorithm to solve sudoku.
    Return the solution.
    '''
    stack = [copy.deepcopy(sudoku)]

    while stack:
        candidate = stack.pop(-1)

        if candidate.is_complete():
            if candidate.validate():
                return candidate
            else:
                continue

        index = candidate.first_empty()
        for i in range(1, 10):
            index.value = i
            index.weight(-1)
            if candidate.validate():
                stack.append(copy.deepcopy(candidate))
                if visualise:
                    candidate.draw()
    return None

def DFS_weight(sudoku, visualise=False):
    '''
    Use DFS algorithm to solve sudoku but start each iteration from the cell with maimum weight. The input needs to be a Board object.
    '''
    stack = [copy.deepcopy(sudoku)]
    while stack:
        candidate = stack.pop(-1)
        candidate.gen_weight()
        
        if candidate.is_complete():
            if candidate.validate():
                return candidate
            else:
                continue

        guess = candidate.max_weight()
        for i in range(1, 10):
            guess.value = i
            guess.weight(-1)
            if candidate.validate():
                stack.append(copy.deepcopy(candidate))
                if visualise:
                    candidate.draw()
    return None

def BFS_solve(sudoku, visualise=False):
    '''
    Use BFS algorithm to solve Sudoku.
    Return the solution.
    '''
    q = [copy.deepcopy(sudoku)]

    while q:
        candidate = q.pop(0)
    
        if candidate.is_complete():
            if candidate.validate():
                return candidate
            else:
                continue

        index = candidate.first_empty()
        for i in range(1, 10):
            index.value = i
            index.weight(-1)
            if candidate.validate():
                q.append(copy.deepcopy(candidate))
                if visualise:
                    candidate.draw()
    return None

def BFS_weight(sudoku, visualise=False):
    '''
    Use BFS algorithm to solve sudoku but start each iteration from the cell with maimum weight. The input needs to be a Board object.
    '''
    q = [copy.deepcopy(sudoku)]
    while q:
        candidate = q.pop(0)
        candidate.gen_weight()
        if candidate.is_complete():
            if candidate.validate():
                return candidate
            else:
                continue

        guess = candidate.max_weight()
        for i in range(1, 10):
            guess.value = i
            guess.weight(-1)
            if candidate.validate():
                q.append(copy.deepcopy(candidate))
                if visualise:
                    candidate.draw()
    return None

def elimination(puzzle, visualise=False):
    '''
    Try to rewrite elimination with Board() and Cell().
    '''
    sudoku = copy.deepcopy(puzzle)

    while not (sudoku.validate() and sudoku.is_complete()):
        sudoku.gen_weight()
        cell = sudoku.max_weight()
        
        if cell.weight() != 8:
            break
        
        elif cell.weight() == 8:
            num_available = [i for i in range(1, 10)]
            
            for i in set([j.value for j in sudoku.row(cell) + sudoku.column(cell) + sudoku.block(cell)]):
                if i in num_available:
                    num_available.remove(i)
            
            cell.value = num_available[0]
            cell.weight(-1)
        
        if visualise:
            sudoku.draw()

    if sudoku.is_complete() and sudoku.validate():
        return sudoku

    elif sudoku.validate():
        cell = sudoku.max_weight()
        num_available = [i for i in range(1, 10)]
        
        for i in set([j.value for j in sudoku.row(cell) + sudoku.column(cell) + sudoku.block(cell)]):
            if i in num_available:
                num_available.remove(i)
        
        candidates = []
        for i in num_available:
            cell.value = i
            cell.weight(-1)
            candidates.append(copy.deepcopy(sudoku))
        
        for i in candidates:
            result = elimination(i, visualise)
            if isinstance(result, Board):
                return result

    elif (not sudoku.validate()) and sudoku.is_complete():
        return None

def batch_solve(algo, list_of_sudoku, visualise=False, cores=max(multiprocessing.cpu_count() // 2, 1), *args):
    '''
    Attempt to solve a list of sudoku simutaneously.
    Return the list of solution in the same order of the input.
    '''
    pool = multiprocessing.Pool(processes=cores)
    result = pool.starmap_async(algo, tuple((i, visualise) for i in list_of_sudoku)).get()
    return result

def load_sudoku(path='puzzles.txt'):
    '''
    Return the arrays stored in a file.
    '''
    fin = open(path, 'r')
    puzzles = fin.readlines()
    fin.close()
    puzzles = Array.clear_item(puzzles, '\n')
    for i in range(len(puzzles)):
        puzzles[i] = eval(puzzles[i])
        puzzles[i] = (puzzles[i][:9], puzzles[i][9])
    return puzzles

def dump_sudoku(array, path='puzzles.txt'):
    '''
    Write an array into a file.
    '''
    fin = open(path, 'r')
    legacy = fin.readlines()
    fin.close()
    fin = open(path, 'w')
    content = Array.clear_item(legacy + array, '\n')
    for i in content:
        fin.write(str(i) + '\n')
    fin.close()

def ask_for_puzzle():
    '''
    Return a list of sudoku entered from console as well as its difficulty.
    The list can be used for dump_sudoku().
    '''
    puzzles = []
    stop = False
    finished = {'y':True,
                'n':False,
                '':True}

    while not stop:
        try:
            puzzle = __enter()
            puzzle.append(input("What's the difficulty of the puzzle: "))
            puzzles.append(puzzle)
            stop = bool(finished[input('Have you finished?(Y/n) ').lower()])
        except KeyboardInterrupt:
            stop = True
            print('\n')
    return puzzles

if __name__ == '__main__':
    '''
    total_time = 0
    algo = brutal_solve

    for puzzle in [x[0] for x in load_sudoku('puzzles.txt')]:
        pprint(puzzle)
        time_spent, result = timer(algo, puzzle, False)
        pprint(result)
        total_time += time_spent
        print('')

    print('Solved in {}s using {}.'.format(total_time, algo.__name__))
    '''
    dump_sudoku(ask_for_puzzle())
    '''
    time_spent, result = timer(batch_solve, [x[0] for x in load_sudoku('puzzles.txt')], BFS_solve, False, 4)
    for i in result:
        pprint(i)
    print('Solved in {}s.'.format(time_spent))
    '''
