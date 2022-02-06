import turtle

window = turtle.Screen()

David = turtle.Turtle()

n = int(input("Enter the number of sides: "))  # the number of sides
d = 500 / n  # the length of each side

David.up()
David.backward(50)
David.right(90)
David.forward(500 / n / 1.7)
David.left(90)
David.down()

for i in range(n):
    David.forward(d)
    David.left(360 / n)
