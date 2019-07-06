import Array, numpy, copy, turtle, time
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
            
def _enter():
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
    
if __name__ == '__main__':
    _sample = [[9,8,0,2,0,0,0,1,0],
               [0,3,6,0,8,1,0,5,0],
               [1,0,0,0,0,5,0,2,0],
               [0,0,0,5,0,0,2,0,1],
               [8,0,0,0,1,0,4,0,0],
               [0,6,0,0,2,0,9,0,0],
               [7,4,3,1,5,0,6,0,0],
               [0,2,0,8,4,0,0,0,7],
               [0,0,0,7,0,3,0,0,2]]

    _correct = [[1,2,3,4,5,6,7,8,9],
                [4,5,6,7,8,9,1,2,3],
                [7,8,9,1,2,3,4,5,6],
                [2,3,4,5,6,7,8,9,1],
                [5,6,7,8,9,1,2,3,4],
                [8,9,1,2,3,4,5,6,7],
                [3,4,5,6,7,8,9,1,2],
                [6,7,8,9,1,2,3,4,5],
                [9,1,2,3,4,5,6,7,8]]

    draw(_correct) 
