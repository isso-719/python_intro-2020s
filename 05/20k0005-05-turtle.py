import turtle


def draw_rect(t, x, y, w, h):
    t.up()
    t.goto(x, y)
    t.down()
    t.goto(x + w, y)
    t.goto(x + w, y + h)
    t.goto(x, y + h)
    t.goto(x, y)


t = turtle.Pen()
for x in range(10):
    p = (x + 1) * -5
    s = (x + 1) * 10
    draw_rect(t, p * 2, p, s * 2, s)
