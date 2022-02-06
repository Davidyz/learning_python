import turtle
import math


def polygon(n, r):
    """this function helps you draw a polygon."""

    window = turtle.Screen()

    david = turtle.Turtle()
    david.pensize(2)

    a = float(360 / n)  # this is the angle the turtle will turn each time
    l = 2 * (math.sin(math.radians(a / 2)) * r)  # this is the length of the sides

    david.penup()
    david.speed(0)
    david.right(90)
    david.forward(r * math.cos(math.radians(a / 2)))
    david.right(90)
    david.forward(l / 2)
    david.left(180)
    david.pendown()
    david.speed(1 / 2)

    for x in range(n):
        david.forward(l)
        david.left(a)


def drop(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


y = int(input("enter the radius here: "))
z = int(input("enter the number of sides here: "))

polygon(z, y)

import time

time.sleep(3)
