import random, math

def get_digit(n, base=10):
    return math.floor(math.log(n, base)) + 1

class Board:
    def __init__(self, x=4, y=None, shell=True):
        if y == None:
            y = x
        self.grid = [[0 for j in range(x)] for i in range(y)]
        self.empty = []
        self.filled = []
        self.gen_empty()
        self.probability_4 = 0.1 # the probability of generating a 4 as new number
        self.game_over = False
        self.shell = shell # True when being tested in ipython or python intepreter. show board after each motion.
        self.new_number()

    def gen_empty(self):
        self.empty = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    self.empty.append((i, j))

    def __str__(self):
        '''
        string = "+" + "--" * len(self.grid[0]) + '-+\n'
        for i in self.grid:
            string += '|'
            for j in i:
                string += ' '
                if j == 0:
                    string += ' '
                else:
                    string += str(j)
            string += ' |\n'
        string += '+' + '--' * len(self.grid[0]) + '-+'
        '''
        string = []
        widths = [max([get_digit(self.grid[row][column]) if self.grid[row][column] != 0 else 0 for row in range(len(self.grid))]) for column in range(len(self.grid[0]))]
        for row in range(len(self.grid)):
            cache = ['|']
            for column in range(len(self.grid[0])):
                if self.grid[row][column]:
                    cache.append(' ' * (widths[column] - get_digit(self.grid[row][column]) + 1) + str(self.grid[row][column]))
                else:
                    cache.append(' ' * widths[column] + ' ')
            cache.append(' |')
            string.append(''.join(cache))
        string.insert(0, '+' + '-' * (len(string[-1]) - 2) + '+')
        string.append('+' + '-' * (len(string[-1]) - 2) + '+')
        return '\n'.join(string)

    def __repr__(self):
        return str(self)

    def new_number(self):
        seed = random.uniform(0, 1)
        if seed >= self.probability_4:
            number = 2
        else:
            number = 4
        try:
            location = random.choice(self.empty)
            self.grid[location[0]][location[1]] = number
            self.empty.remove(location)
            self.filled.append(location)
        except IndexError:
            self.game_over = True

    def left(self):
        for i in range(len(self.grid)):
            done = False
            index = 0
            while not done:
                modified = False
                for index in range(len(self.grid[i]) - 1):
                    if self.grid[i][index] == 0 and self.grid[i][index + 1] != 0:
                        self.grid[i][index], self.grid[i][index + 1] = self.grid[i][index + 1], self.grid[i][index]
                        done = False
                        modified = True
                    elif self.grid[i][index] and self.grid[i][index] == self.grid[i][index + 1]:
                        modified = True
                        self.grid[i][index] *= 2
                        self.grid[i][index + 1] = 0
                if not modified:
                    done = True
        self.gen_empty()
        self.new_number()
        if self.shell:
            print(str(self))

    def right(self):
        for i in range(len(self.grid)):
            done = False
            index = 0
            while not done:
                modified = False
                for index in range(len(self.grid[i]) - 1):
                    if self.grid[i][index + 1] == 0 and self.grid[i][index] != 0:
                        self.grid[i][index], self.grid[i][index + 1] = self.grid[i][index + 1], self.grid[i][index]
                        done = False
                        modified = True
                    elif self.grid[i][index] and self.grid[i][index] == self.grid[i][index + 1]:
                        modified = True
                        self.grid[i][index + 1] *= 2
                        self.grid[i][index] = 0
                if not modified:
                    done = True
        self.gen_empty()
        self.new_number()
        if self.shell:
            print(str(self))

    def up(self):
        for i in range(len(self.grid[0])):
            done = False
            index = 0
            while not done:
                modified = False
                for index in range(len(self.grid) - 1):
                    if self.grid[index][i] == 0 and self.grid[index + 1][i] != 0:
                        self.grid[index][i], self.grid[index + 1][i] = self.grid[index + 1][i], self.grid[index][i]
                        done = False
                        modified = True
                    elif self.grid[index][i] and self.grid[index][i] == self.grid[index + 1][i]:
                        modified = True
                        self.grid[index][i] *= 2
                        self.grid[index + 1][i] = 0
                if not modified:
                    done = True
        self.gen_empty()
        self.new_number()
        if self.shell:
            print(str(self))

    def down(self):
        for i in range(len(self.grid[0])):
            done = False
            index = 0
            while not done:
                modified = False
                for index in range(len(self.grid) - 1):
                    if self.grid[index][i] != 0 and self.grid[index + 1][i] == 0:
                        self.grid[index][i], self.grid[index + 1][i] = self.grid[index + 1][i], self.grid[index][i]
                        done = False
                        modified = True
                    elif self.grid[index][i] and self.grid[index][i] == self.grid[index + 1][i]:
                        modified = True
                        self.grid[index + 1][i] *= 2
                        self.grid[index][i] = 0
                if not modified:
                    done = True
        self.gen_empty()
        self.new_number()
        if self.shell:
            print(str(self))
