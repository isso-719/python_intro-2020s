# Question1
from dataclasses import *
@dataclass
class Rect:
    x: str
    y: str
    w: str
    h: str


# Question2
def area_rect(rect):
    result = rect.w * rect.h
    return result


# Question3
def map_area_rect(rects):
    result = []
    for x in rects:
        result.append(area_rect(x))
    return result


rectangles = [
    Rect(0, 0, 2, 4),
    Rect(0, 0, 4, 4),
    Rect(0, 0, 3, 2)
]
print("問題3")
print(map_area_rect(rectangles))


# Question4
def filter_rect_20(rects):
    result = []
    for x in rects:
        if area_rect(x) >= 20:
            result.append(area_rect(x))
    return result


print("問題4")
print(filter_rect_20(rectangles))


# Question5
def fold_plus(values):
    result = 0
    for x in values:
        result = result + x
    return result


print("問題5")
print(fold_plus(map_area_rect(rectangles)))


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
