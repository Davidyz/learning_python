import turtle

def star(n):
    window = turtle.Screen()
    david = turtle.Turtle()

    david.pensize(2)

    david.up()
    david.goto(-n/2,-n/2/3**0.5)
    david.down()

    for i in range(5):
        david.forward(n)
        david.left(144)
        
a = int(input("enterthe length of the sides: "))

star(a)
