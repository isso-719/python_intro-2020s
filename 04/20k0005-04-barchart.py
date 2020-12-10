import turtle

i = input("値を入力>")
val = eval(i)

t = turtle.Pen()
t.forward(10)

for x in val:
    t.left(90)
    t.forward(x)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(x)
    t.left(90)
    t.forward(10)

t.left(90)
t.left(90)
t.forward(10 * (len(val) * 2 + 2))
