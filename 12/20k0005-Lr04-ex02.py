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
    Rect(0, 0, 3, 2),
    Rect(0, 0, 4, 6)
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
