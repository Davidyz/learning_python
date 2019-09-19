import turtle
class Cell(turtle.Turtle):
    def __init__(self, mine):
        turtle.Turtle.__init__(self)
        self.__mine = mine
        self.__adj = 0

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
        pass
