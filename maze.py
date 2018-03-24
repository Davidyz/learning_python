#!/usr/bin/python3
import turtle, time

layout = ["wwwwwwwwwwwwwwwwwwww",
          "wp wwwwwwwwwwwww   w",
          "ww               w w",
          "wwwwfwwwwwwwwwwwww w",
          "wwww wwwww   ww    w",
          "wwww w   www ww wwww",
          "wwww   w www ww wwww",
          "wwwwwwww www       w",
          "www   c  wwwwwwwww w",
          "www wwwwwwwwwfcfww w",
          "wwwfwwwwwwwwwfwfww w",
          "w                w w",
          "wwwwwwwwwwwwwwww w w",
          "wwwwwwwwwwwwwwww w w",
          "wwww             w w",
          "wwwwfwww wwwwwwwww w",
          "wwww www           w",
          "wwww wwwwwwwwwwwwwww",
          "wwww              tw",
          "wwwwwwwwwwwwwwwwwwww"]

def item(x,y,category,fake = False):
    global coins
    t = "n" + str(x) + str(y)
    t = turtle.Turtle()
    t.penup()
    t.shapesize(1.5,1.5)
    t.speed(0)
    
    if category == "block":
        t.shape("square")
        t.color("brown")
        if not fake:
            walls.append(t)

    if category == "coin":
        t.shape("circle")
        t.shapesize(1,1)
        t.color("yellow")
        coins.append(t)
    t.goto(-285 + y * 30, 285 - x * 30)

walls = []
coins = []

def map_generator(layout):
    global target_cor
    for row in range(0, len(layout)):
        for column in range(0,len(layout[row])):
            
            if layout[row][column] == "w":
                item(row, column, "block")
                #walls.append([row,column])
            
            if layout[row][column] == "p":
                player.goto(-285 + column * 30, 285 - row * 30)
            
            if layout[row][column] == "f":
                item(row, column, "block",True)

            if layout[row][column] == "c":
                item(row, column, "coin")
                #coins.append([row,column])

            if layout[row][column] == "t":
                target.goto(-285 + column * 30, 285 - row * 30)
                #target_cor = [row,column]

def return_cor(item):
    """
    convert the list of coordinates of an object into
    the coordinates in pixels.
    """
    return [-285 + item[1] * 30, 285 - item[0] - 30]

def left():
    player.setheading(180)
    player.goto(player.xcor() - 5, player.ycor())

def right():
    player.setheading(0)
    player.goto(player.xcor() + 5, player.ycor())

def up():
    player.setheading(90)
    player.goto(player.xcor(), player.ycor() + 5)

def down():
    player.setheading(270)
    player.goto(player.xcor(), player.ycor() - 5)

def start_up():
    window.onkey(left, "Left")
    window.onkey(right, "Right")
    window.onkey(up, "Up")
    window.onkey(down, "Down")
    window.listen()
    window.update()

def catch(turtle):
    """
    return the distance between player and target.
    """
    return ((player.xcor() - turtle.xcor()) ** 2 + (player.ycor() - turtle.ycor()) ** 2) ** 0.5

def goal_detect():
    """
    return True if player has touched the target.
    require the 'catch()' function.
    """
    if catch(target) < 15:
        return True

def distance(item):
    """
    return the distance between player and an item whose coordinates are represented in terms
    of a list.
    require the 'return_cor()' function.
    eg, walls,
        coins.
    """
    return ((player.xcor() - return_cor(item)[0]) ** 2 + (player.ycor() - return_cor(item)[1]) ** 2) ** 0.5


def introduction():
    print("Hey! Welcom to my first maze game!")
    time.sleep(1)
    print("You are controlling the black arrow using the direction keys on your keyboard.")
    time.sleep(2)
    print("Your target is the red circle at the corner.")
    time.sleep(2)
    print("Tips:\nif you want to win,\nyou will have to find the hiden ways to go through the wall.")
    time.sleep(2)
    print("Ready?")
    time.sleep(1)
    print("Go!")

def new_direction():
    window.onkey(player.left(90), "Left")
    window.onkey(player.right(90), "Right")

introduction()

window = turtle.Screen()

player = turtle.Turtle()
player.speed(0)
player.shapesize(1,1)
player.penup()

window.tracer(0)

target = turtle.Turtle()
target.shape("circle")
target.shapesize(1,1)
target.color("red")
target.setheading(0)
target.speed(0)
target.penup()
map_generator(layout)

finished = True

while finished == True:
    start_up()
    if goal_detect():
        target.color('green')
        print("You've won the game!")
        time.sleep(5)
        finished = False
    for i in coins:
        if catch(i) < 15:
            print("you got a coin!")
            i.goto(100000,0)
    for i in walls:
        if catch(i) < 20:
            player.backward(5)
    window.update()

