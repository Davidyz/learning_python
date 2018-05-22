#ball collisions using class
import turtle, time, math, random

window = turtle.Screen()
window.tracer(0,0)

width = 600
height = 400

class Ball(turtle.Turtle):
    def __init__(self, color, v_x, v_y):
        turtle.Turtle.__init__(self)
        self.penup()
        self.color(color)
        self.shape("circle")
        self.speed(0)

        self.velocity = [v_x, v_y]
        self.new_coordinates = [0,0]
        #perhaps will use later, keep default for now
        self.mass = 1
        self.radius = 10

    def calculate_new_coordinates(self):
        self.new_coordinates[0] = self.xcor() + self.velocity[0]
        self.new_coordinates[1] = self.ycor() + self.velocity[1]

    def move_ball(self):
        self.goto(self.new_coordinates[0], self.new_coordinates[1])

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
    ball.calculate_new_coordinates()
    x = ball.new_coordinates[0]  #save writing this again
    y = ball.new_coordinates[1]
    r = ball.radius
    if x+r > width/2 or x-r < -width/2:
        ball.velocity[0] = -1*ball.velocity[0]
        ball.calculate_new_coordinates()

    if y+r > height/2 or y-r < -height/2:
        ball.velocity[1] = -1*ball.velocity[1]
        ball.calculate_new_coordinates()

def check_ball_collision(ball1, ball2):
    dx = (ball2.xcor() - ball1.xcor())
    dy = (ball2.ycor() - ball1.ycor())
    distance = math.sqrt(dx**2 + dy**2)
    R = ball1.radius + ball2.radius
    u1x = ball1.velocity[0]
    u1y = ball1.velocity[1]
    u2x = ball2.velocity[0]
    u2y = ball2.velocity[1]

    if distance <= R:
        """
        u1 = math.sqrt(ball1.velocity[0]**2 + ball1.velocity[1]**2)
        u2 = math.sqrt(ball2.velocity[0]**2 + ball2.velocity[1]**2)
        alpha = math.atan(dy/dx)
        r1 = abs(u1*math.sin(alpha))
        r2 = abs(u1*math.cos(alpha))
        ball1.velocity = [(r1/R)*dy,-(r1/R)*dx]
        ball2.velocity = [(r2/R)*dx,(r2/R)*dy]
        """
        ball1.velocity = [u2x, u2y]
        ball2.velocity = [u1x, u1y]
        ball1.calculate_new_coordinates()
        ball2.calculate_new_coordinates()
        

ball_1 = Ball("red", 2, 1)
ball_1.goto(-width/4, -5) 

ball_2 = Ball("blue", 2, 3)
ball_2.goto(width/4, 0)

ball_3 = Ball("green", 1, 1)

ball_4 = Ball("orange", 1, 3)
ball_4.goto(0, height/4)

while True:
    ball_1.calculate_new_coordinates()
    checkboundary(ball_1)
    ball_2.calculate_new_coordinates()
    checkboundary(ball_2)
    ball_3.calculate_new_coordinates()
    checkboundary(ball_3)
    ball_4.calculate_new_coordinates()
    checkboundary(ball_4)
    check_ball_collision(ball_1, ball_2)
    check_ball_collision(ball_1, ball_3)
    check_ball_collision(ball_1, ball_4)
    check_ball_collision(ball_2, ball_3)
    check_ball_collision(ball_2, ball_4)
    check_ball_collision(ball_3, ball_4)
    ball_1.move_ball()
    ball_2.move_ball()
    ball_3.move_ball()
    ball_4.move_ball()


    window.update()

    time.sleep(1/120)
