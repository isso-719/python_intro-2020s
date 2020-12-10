# Question1
from dataclasses import *
@dataclass
class Rect:
    x: str
    y: str
    w: str
    h: str


# Question1
def includes_point(r, x, y):
    if r.x <= x and x <= r.x + r.w:
        if r.y <= y and y <= r.y + r.h:
            return True

    return False


print("問題1")
print(includes_point(Rect(0, 0, 2, 2), 1, 1))
print(includes_point(Rect(0, 0, 2, 2), 3, 3))


# Question2
def includes_rect(r1, r2):
    r2x1 = r2.x
    r2y1 = r2.y
    r2x2 = r2.x + r2.w
    r2y2 = r2.y + r2.h

    if includes_point(r1, r2x1, r2y1) == True and includes_point(r1, r2x2, r2y2) == True:
        return True

    return False


r1 = Rect(-1, -1, 4, 4)
r2 = Rect(0, 0, 2, 2)
print("問題2")
print(includes_rect(r1, r2))  # True が表示される。
# 以下別の例も各自作成し、結果を試すこと。

r1 = Rect(-1, -1, 4, 4)
r2 = Rect(0, 0, 5, 5)
print(includes_rect(r1, r2))
