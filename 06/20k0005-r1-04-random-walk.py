import random
import turtle

t = turtle.Pen()

for x in range(100):

    t.forward(20)

    r = random.random() * 2

    if r < 1.0:
        t.left(45)

    else:
        t.left(-45)
