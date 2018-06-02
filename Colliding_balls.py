#ball collisions using class
#try to optomise the collision detecting algorithm
### try divide into 4 horizontal sections s
import turtle, time, math, random, itertools

N = 50 #number of balls

window = turtle.Screen()
window.tracer(0,0)

width = 600
height = 400

colors = ['red','blue','green','yellow','orange','black','purple',
          'lightblue','pink']

balls = [] #store ball objects as dictionary

starting_posns = []

class Ball(turtle.Turtle):
    def __init__(self, color, v_x, v_y):
        #global balls
        turtle.Turtle.__init__(self)
        self.penup()
        self.color(color)
        self.shape("circle")
        self.speed(0)

        self.velocity = [v_x, v_y]
        self.new_coordinates = [0,0]
        self.SPEED = 1 #choose values later
        #perhaps will use later, keep default for now
        self.mass = 1
        self.radius = 9
        self.hit_boundary = False
        self.collided = False
        self.distance = math.sqrt((self.xcor() + 300) ** 2 + (self.ycor() + 200) ** 2) #(-300, -200) is the imagined origin for checking collision.

    def calculate_new_coordinates(self):
        # normalise velocity component then mult by SPEED
        magnitude = math.sqrt(self.velocity[0]**2 + self.velocity[1]**2)
        if magnitude != 0:
            a = self.SPEED/magnitude
            self.new_coordinates[0] = self.xcor() + a*self.velocity[0]
            self.new_coordinates[1] = self.ycor() + a*self.velocity[1]
        else:
            self.new_coordinates[0] = self.xcor() + self.velocity[0]
            self.new_coordinates[1] = self.ycor() + self.velocity[1]

    def move_ball(self):
        self.goto(self.new_coordinates[0], self.new_coordinates[1])

    def change_size(self):
        self.shapesize(self.radius/10)

#make border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(3)
border.penup()
border.goto(-width/2,-height/2)
border.pendown()
for i in range(2):
    border.forward(width)
    border.left(90)
    border.forward(height)
    border.left(90)

#check boundary
def checkboundary(ball):
    ball.hit_boundary = False
    ball.calculate_new_coordinates()
    x = ball.new_coordinates[0]  #save writing this again
    y = ball.new_coordinates[1]
    r = ball.radius + 1 #(+ padding)
    if x+r > width/2 or x-r < -width/2:
        ball.velocity[0] = -1*ball.velocity[0]
        ball.calculate_new_coordinates()
        ball.hit_boundary = True

    if y+r > height/2 or y-r < -height/2:
        ball.velocity[1] = -1*ball.velocity[1]
        ball.calculate_new_coordinates()
        ball.hit_boundary = True

def check_ball_collision(ball1, ball2):
    global balls
    dx = (ball2.new_coordinates[0] - ball1.new_coordinates[0])
    dy = (ball2.new_coordinates[1] - ball1.new_coordinates[1])
    #dx = (ball2.xcor() - ball1.xcor())
    #dy = (ball2.ycor() - ball1.ycor())
    distance = math.sqrt(dx**2 + dy**2)
    R = ball1.radius + ball2.radius + 3 ###
    u1x = ball1.velocity[0]
    u1y = ball1.velocity[1]
    u2x = ball2.velocity[0]
    u2y = ball2.velocity[1]

    if distance <= R:
        if ball1.hit_boundary == True or ball2.hit_boundary == True:
            print("Hit boundary and collided")
        ball1.SPEED, ball2.SPEED = ball2.SPEED, ball1.SPEED
        ball1.velocity = [u2x, u2y]
        ball2.velocity = [u1x, u1y]
        ball1.calculate_new_coordinates()
        ball2.calculate_new_coordinates()

def check_distance(a,b):
    '''Distances between two coordinates a and b'''
    dx = a[0]-b[0]
    dy = a[1]-b[1]
    return math.sqrt(dx**2 + dy**2)

       
def gen_random_start():
    x = random.randint(-(width/2)+10, (width/2)-10)
    y = random.randint(-(height/2)+10, (height/2)-10)
    return x,y
    
def generate_n_balls(n):
    '''generates n balls, stores in dictionary'''
    global balls, starting_posns
    for i in balls:
        #choose random color and velocities
        color = colors[random.randint(0,len(colors)-1)]
        vx = random.randint(-5,5)
        vy = random.randint(-5,5)
        i = Ball(color, vx, vy)
        i.SPEED = random.random() + random.randint(0,2) ###
        #balls[i].change_size()

        #set random position
        unique = False
        while unique == False:
            distances_ok = True
            x,y = gen_random_start()
            if len(starting_posns) == 0:
                starting_posns.append([x,y])
                unique = True
                break

            else:
                for b in starting_posns:
                    if check_distance([x,y],b) < 25:
                        distances_ok = False
                        break

            if distances_ok == True:
                starting_posns.append([x,y])
                unique = True
                     
        i.setposition(x,y)
        
def quicksort(array):
    '''
    Sort the balls in the order of their distance to the imagined origin.
    '''
    if len(array) < 2:
        return array

    pivot = array[-1].distance()
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i].distance() <= pivot:
            i += 1
        elif array[i].distance() > pivot:
            array.insert(-1, array.pop(i))
            j -= 1
    return quicksort(array[:j]) + [pivot] + quicksort(array[j:len(array) - 1])

#combinations = list(itertools.combinations([x for x in range(1,N+1)],2))

###check initial posns
min_d = 100
def check_initial_positions():
    global starting_posns
    min_d = 100
    for c in balls:#combinations:
        r = check_distance(starting_posns[c - 1],starting_posns[c[1]-1])
        if r < min_d:
            min_d = r
    return min_d


# generate N balls
generate_n_balls(N)

#print(check_initial_positions())

while True:
    balls = quicksort(balls)

    for ball in balls:
        ball.calculate_new_coordinates()
        checkboundary(ball)
    
    for i in range(0, len(balls) - 1):
        if balls[i + 1].distance() - balls[i].distance() < 18:
            check_ball_collision(balls[i], balls[i + 1])
        else:
            pass

    for i in balls:
        i.move_ball()
    
    window.update()
    time.sleep(1/120)
"""
while True:
    for ball in balls:
        balls[ball].calculate_new_coordinates()
        checkboundary(balls[ball])
        
    #check for collisions
    for c in combinations:
        check_ball_collision(balls[c[0]],balls[c[1]])


    #move balls
    for ball in balls:
        balls[ball].move_ball()


    window.update()

    #time.sleep(1/120)
"""
