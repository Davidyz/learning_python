import turtle
import time

window = turtle.Screen()

window.setup(900,600)

evin = turtle.Turtle()

evin.color("red")

evin.penup()
evin.pensize(2)
evin.right(90)

evin.forward(100)

evin.left(90)

evin.pendown()
evin.circle(100)

evin.penup()
evin.goto(0,0)
evin.hideturtle()

#codes of evin end here

david = turtle.Turtle()

david.shape("turtle")

david.color("green")

david.penup()

david.pensize(3)

for x in range(12):

    if david.heading() == 90:
        david.stamp()

    david.forward(60)
    david.pendown()
    david.forward(20)
    david.penup()
    david.forward(20)
    david.stamp()
    david.backward(100)
    david.left(30)

david.hideturtle()

time.sleep(2)
