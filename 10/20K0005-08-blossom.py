import turtle
t = turtle.Turtle()

s = input("3以上の整数を入力してください！>>")

spin = (180 * (int(s) - 2)) / int(s)

t.fillcolor('pink')
t.begin_fill()

for x in range(int(s)):
    t.left(90)
    t.forward(100)
    t.right(120)
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.right(120)
    t.forward(100)
    t.left(spin - 90)

t.end_fill()
