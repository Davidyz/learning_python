import turtle, random
class Cell(turtle.Turtle):
    def __init__(self, location=[0, 0], dimension=10, mine=False):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color('brown')
        self.shape('square')
        self.shapesize(28 / dimension)
        self.speed(0)

        self.goto(-300 + 1/2 * (600 / dimension) + 600 / dimension * location[0], -300 + 1/2 * (600 / dimension) + 600 / dimension * location[1])
        self.__mine = mine
        self.__adj = 0
        self.__location = location

    def row(self):
        return self.__location[0]

    def column(self):
        return self.__location[1]

    def IsMine(self):
        return self.__mine
    
    def AdjacentMines(self, num=None):
        if not isinstance(num, int):
            return
        if num == None:
            return self.__adj
        else:
            self.__adj = num

class Map():
    def __init__(self, mines):
        """
        mines being a 2D list.
        """
        self.__map = mines
        self.__size = len(mines), len(mines[0])
    
    def __list__(self):
        temp = []
        for i in self.__map:
            temp += i
        return temp

    def __dict__(self):
        """
        Return the adjacent cells of a cell in terms of a dict.
        """
        data = {}
        all_cells = list(self)

        for cell in all_cells:
            temp = list(self)
            for i in temp:
                if not ((0 < abs(i.row() - cell.row()) < 2) and (0 < abs(i.column() - cell.column()) < 2)):
                    temp.remove(i)
                    data[cell] = temp
        return data

    def map(self):
        return self.__map

    def size(self):
        return self.__size

def GenMap(dimension, number=None):
    total_cell = dimension ** 2

    if number == None:
        number = total_cell // 10
    b = [True for i in range(number)] + [False for i in range(total_cell)]
    random.shuffle(b)

    m = [[] for i in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            m[i].append(Cell([i, j], dimension, b.pop(0)))

    return Map(m)

if __name__ == '__main__':
    m = [[] for i in range(10)]
    
    for i in range(10):
        for j in range(10):
            m[i].append(Cell([i, j]))
    board = Map(m)
