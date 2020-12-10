import turtle

t = turtle.Turtle()

t.fillcolor('yellow')
t.begin_fill()

t.right(60)

for x in range(6):
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.right(45)
    t.circle(10)
    t.right(75)

t.end_fill()
