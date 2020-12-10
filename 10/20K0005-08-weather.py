from dataclasses import *
import turtle

# タートル初期化
t = turtle.Turtle()

# モデリング
@dataclass
class Temp:
    high: str
    low: str


# 1週間の気温情報
weathers = [Temp(27.2, 18),
            Temp(24.5, 19.3),
            Temp(21, 17.7),
            Temp(26.1, 19.4),
            Temp(29.3, 21.2),
            Temp(28.4, 21),
            Temp(29.4, 20.9)]

# 描く
t.forward(20)
for weather in weathers:
    t.fillcolor('red')
    t.begin_fill()

    t.left(90)
    t.forward(weather.high * 5)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(weather.high * 5)
    t.right(90)
    t.forward(40)

    t.end_fill()

    t.right(180)
    t.forward(20)

    t.fillcolor('blue')
    t.begin_fill()
    t.left(90)
    t.forward(weather.low * 5)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(weather.low * 5)
    t.right(90)
    t.forward(30)
    t.end_fill()

    t.right(180)
    t.forward(60)
