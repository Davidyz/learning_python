#!/usr/bin/python3
import turtle, time

"""
My first maze game!
"""
layout = [
    "wwwwwwwwwwwwwwwwwwww",
    "wp wwwwwwwwwwwww   w",
    "ww               w w",
    "ww w wwwwwwwwwwwww w",
    "ww w wwwww   ww    w",
    "ww w w   www ww wwww",
    "w  w   w w w ww wwww",
    "w wwwwww www       w",
    "w w   c   wwwwwwww w",
    "w w wwwww   w c ww w",
    "www wwwwwwwww w ww w",
    "w             w  w w",
    "w wwwwwwwwwwwwww w w",
    "w wwwwwwwwwwwwww w w",
    "w ww             w w",
    "w ww wwwwwwwwwwwww w",
    "w ww w             w",
    "w ww wwwwwwwwwwwwwww",
    "w ww              tw",
    "wwwwwwwwwwwwwwwwwwww",
]

layout1 = [
    "wwwwwwwwwwwwwwwwwwww",
    "wpwwww    c        w",
    "w      wwwwwwwwwww w",
    "www wwwwwwwwwwww w w",
    "www ww      wwww w w",
    "www    wwww wwww w w",
    "wwwwwwwwwww  www   w",
    "wwwwwwwwwwww wwwwwww",
    "w            ww wwww",
    "w w wwwwwwwwwww   ww",
    "w w wwwwwwwwwww wwww",
    "w w         c      w",
    "w ww wwwwwwwwwwww ww",
    "w ww           ww ww",
    "w wwwwwwwwwwww ww ww",
    "w            w ww ww",
    "wwwwwwwwwwww w ww ww",
    "wwwwwwwwwwww w    ww",
    "wt           wwwwwww",
    "wwwwwwwwwwwwwwwwwwww",
]

list_of_layout = [layout, layout1]


def item(x, y, category, fake=False):
    """
    Move the items to the corresponding place.
    """
    global coins
    t = "n" + str(x) + str(y)
    t = turtle.Turtle()
    t.penup()
    t.shapesize(1.5, 1.5)
    t.speed(0)

    if category == "block":
        t.shape("square")
        t.color("brown")
        walls["n" + str(x)].append(t)

    if category == "coin":
        t.shape("circle")
        t.shapesize(1, 1)
        t.color("yellow")
        coins.append(t)
    t.goto(-285 + y * 30, 285 - x * 30)


def map_generator(layout):
    """
    Convert the layout list to the graphical UI.
    """
    global target_cor
    for row in range(0, len(layout)):
        for column in range(0, len(layout[row])):

            if layout[row][column] == "w":
                item(row, column, "block")

            if layout[row][column] == "p":
                player.goto(-285 + column * 30, 285 - row * 30)

            if layout[row][column] == "f":
                item(row, column, "block", True)

            if layout[row][column] == "c":
                item(row, column, "coin")

            if layout[row][column] == "t":
                target.goto(-285 + column * 30, 285 - row * 30)


def return_cor(item):
    """
    Convert the list of coordinates of an object into the coordinates in pixels.
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
    Return the distance between player and target.
    """
    return (
        (player.xcor() - turtle.xcor()) ** 2 + (player.ycor() - turtle.ycor()) ** 2
    ) ** 0.5


def goal_detect():
    """
    Return True if player has touched the target.
    Require the 'catch()' function.
    """
    if catch(target) < 15:
        return True


def distance(item):
    """
    Return the distance between player and an item whose coordinates are represented in terms of a list.
    Require the 'return_cor()' function.
    Eg, walls, coins.
    """
    return (
        (player.xcor() - return_cor(item)[0]) ** 2
        + (player.ycor() - return_cor(item)[1]) ** 2
    ) ** 0.5


def introduction():
    print("Hey! Welcom to my first maze game!")
    time.sleep(1)
    print(
        "You are controlling the black arrow using the direction keys on your keyboard."
    )
    time.sleep(2)
    print("Your target is the red circle at the corner.")
    time.sleep(2)
    print("Ready?")
    time.sleep(1)
    print("Go!")
    time.sleep(0.5)


def new_direction():
    window.onkey(player.left(90), "Left")
    window.onkey(player.right(90), "Right")


def coin_caught(t):
    t.speed(1)
    t.goto(-380, 100 * len(coins))
    t.speed(0)
    coins.pop(coins.index(t))


def current_row():
    """
    Return the numbers of rows that the player is in (current one, above one and beneath one), so that when detecting collision with the wall, time consumption can be reduced.
    According to my test, cpu usage will not be improved.
    """
    y = player.ycor()
    current = int((300 - y) // 30)
    return ("n" + str(current - 1), "n" + str(current), "n" + str(current + 1))


if __name__ == "__main__":
    introduction()
    proceed = True
    level = 0
    while proceed == True:
        window = turtle.Screen()
        player = turtle.Turtle()
        player.speed(0)
        player.shapesize(1, 1)
        player.penup()
        walls = {}
        coins = []

        for i in range(21):
            walls["n" + str(i)] = []

        window.tracer(0)
        target = turtle.Turtle()
        target.shape("circle")
        target.shapesize(1, 1)
        target.color("red")
        target.setheading(0)
        target.speed(0)
        target.penup()
        map_generator(list_of_layout[level])
        finished = False

        while not finished:
            start_up()
            if player.ycor() < -240:
                if goal_detect():
                    target.color("green")
                    print("You've won the game!")
                    time.sleep(3)
                    finished = True
            for i in coins:
                if catch(i) < 15:
                    print("you got a coin!")
                    coin_caught(i)
            for (
                i
            ) in (
                current_row()
            ):  # The rows to be scanned is specified so that the time consumption can be reduced.
                for j in walls[i]:
                    if catch(j) < 20:
                        player.backward(5)
        window.bye()

        if input("Do you want to try the next level?(y/n): ") == "n":
            proceed = False
        else:
            level += 1
            if level > len(list_of_layout) - 1:
                proceed = False
