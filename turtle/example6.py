import turtle
from math import *
import time

window = turtle.Screen()
david = turtle.Turtle()
david.pensize(2)


def polygon(turtle, n, r):
    a = float(360 / n)  # this is the angle the turtle will turn each time
    l = 2 * (sin(radians(a / 2)) * r)  # this is the length of the sides

    turtle.penup()
    turtle.speed(0)
    turtle.right(90)
    turtle.forward(r * cos(radians(a / 2)))
    turtle.right(90)
    turtle.forward(l / 2)
    turtle.left(180)
    turtle.pendown()
    turtle.speed(1 / 2)

    for x in range(n):
        turtle.forward(l)
        turtle.left(a)


def drop(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


z = int(input("enter the radius here: "))
y = int(input("enter the number of sides here: "))
m = int(input("enter the degrees of rotating: "))

square = [[100, 100], [-100, 100], [-100, -100], [100, -100]]


def draw(turtle, m):
    for i in range(len(square)):

        xn = square[i][0] * cos(radians(m)) - square[i][1] * sin(radians(m))
        yn = square[i][0] * sin(radians(m)) + square[i][1] * cos(radians(m))
        # new coordinates after rotating

        drop(turtle, xn, yn)
        polygon(turtle, y, z)
        turtle.hideturtle()


draw(david, m)
time.sleep(10)
