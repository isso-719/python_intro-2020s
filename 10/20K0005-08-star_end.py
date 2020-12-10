import turtle

t = turtle.Turtle()

t.fillcolor('yellow')
t.begin_fill()

t.left(72)

for x in range(5):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)

t.end_fill()
