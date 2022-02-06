import maths, turtle, time


def draw(pen, shape):
    pen.penup()
    for i in shape.columns():
        pen.goto(100 * j for j in i[:2])
        pen.pendown()
    pen.penup()


def animated(pen, shape, func, arg, step=100):
    """
    Does not work for amplification yet.
    Can be used to animate rotations.
    """
    for i in range(step):
        pen.hideturtle()
        pen.getscreen().tracer(1, 1)
        pen.speed(0)
        draw(pen, func(i * arg / step) * shape)
        time.sleep(1 / 60)
        pen.reset()
    draw(pen, func(arg) * shape)


drawer = turtle.Turtle()
shape = maths.Matrix(
    [[0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 0, 0, -1, -1, 0]]
)

translation = lambda x=0, y=0: maths.Matrix([[1, 0, x], [0, 1, y], [0, 0, 1]])

rotation_x = lambda a=0: maths.Matrix(
    [[1, 0, 0], [0, maths.cos(a), -maths.sin(a)], [0, maths.sin(a), maths.cos(a)]]
)

rotation_y = lambda a=0: maths.Matrix(
    [[maths.cos(a), 0, maths.sin(a)], [0, 1, 0], [-maths.sin(a), 0, maths.cos(a)]]
)

rotation_z = lambda a=0: maths.Matrix(
    [[maths.cos(a), -maths.sin(a), 0], [maths.sin(a), maths.cos(a), 0], [0, 0, 1]]
)


def amplify(multiple=1):
    return maths.Matrix([[multiple, 0, 0], [0, multiple, 0], [0, 0, multiple]])


translated = translation(1, 0) * shape
rotated = rotation_x(maths.pi / 4) * rotation_y(maths.pi / 4) * shape

animated(drawer, shape, rotation_y, maths.pi / 4, 100)
shape = rotation_y(maths.pi / 4) * shape
animated(drawer, shape, amplify, 2)
time.sleep(3)
