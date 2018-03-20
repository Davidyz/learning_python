import turtle,math,time

b = turtle.Turtle()
a = turtle.Turtle()

a.penup()
b.penup()
a.goto(-200,70)

window = turtle.Screen()
window.tracer(0,0)

a.shape('circle')
b.shape('circle')
a.speed(0)

a.shapesize(5)
b.shapesize(5)

def detect(m,n):
    distance = math.sqrt((m.xcor() - n.xcor()) ** 2 + (m.ycor() - n.ycor()) ** 2)
    if distance < 100:
        return True
    elif distance >= 100:
        return False
    window.update()

a.ondrag(a.goto)
while True:
    if detect(a,b) == True:
        a.color('red')
    elif detect(a,b) == False:
        a.color('black')
    time.sleep(0.01)
    #window.tracer(1,1)
    window.update()
