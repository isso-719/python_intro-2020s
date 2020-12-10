import math
import turtle
from dataclasses import *


@dataclass
class Grade:
    name: str
    mathmatic: int
    physics: int
    english: int


def rader(target):
    for i in people:
        if i.name == target:
            mathmatic = i.mathmatic
            physics = i.physics
            english = i.english

    m_x = mathmatic * math.sin(math.radians(90))
    m_y = mathmatic * math.cos(math.radians(90))
    p_x = physics * math.sin(math.radians(210))
    p_y = physics * math.cos(math.radians(210))
    e_x = english * math.sin(math.radians(330))
    e_y = english * math.cos(math.radians(330))

    t = turtle.Pen()
    t.goto(100 * math.sin(math.radians(90)), 100 * math.cos(math.radians(90)))
    t.write("math(max:100)")
    t.up()
    t.goto(0, 0)
    t.down()
    t.goto(100 * math.sin(math.radians(210)),
           100 * math.cos(math.radians(210)))
    t.write("physics(max:100)")
    t.up()
    t.goto(0, 0)
    t.down()
    t.goto(100 * math.sin(math.radians(330)),
           100 * math.cos(math.radians(330)))
    t.write("english(max:100)")
    t.up()
    t.goto(m_x, m_y)
    t.down()
    t.goto(p_x, p_y)
    t.goto(e_x, e_y)
    t.goto(m_x, m_y)


people = [Grade("Alice", 100, 65, 57),
          Grade("Bob", 45, 98, 100),
          Grade("Charley", 50, 50, 50),
          Grade("Aimi", 100, 100, 100),
          Grade("Ex", 100, 100, 100)]


target = input("誰の成績をみたいですか?>>")
rader(target)
