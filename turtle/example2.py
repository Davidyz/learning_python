import turtle
import time

window=turtle.Screen()

David=turtle.Turtle()

n = int(input("Enter the number of sides: ")) #the number of sides
d = 500/n #the length of each side

David.color("red","green")
David.begin_fill()

David.up()
David.goto(-d/2,-d/2/3**0.5)
David.down()

for i in range(n):
    David.forward(d)
    David.left(360/n)

David.end_fill()

time.sleep(3)
