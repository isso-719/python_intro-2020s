import turtle
t = turtle.Turtle()


def drawSquare(b):
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(25)
        t.left(90)
    t.end_fill()


for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            color = t.color((1, 1, 1))
        else:
            color = t.color((0.0, i / 10, j / 10))
        t.penup()
        t.goto((i - 4) * 25, (j - 4) * 25)
        drawSquare(color)
