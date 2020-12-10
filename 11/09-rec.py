# while True:
#     i = input("入力>")
#     if i == "":
#         print("終了します")
#         break
#     print(f"入力したのは...{i}")

# while True:
#     i = input("よろしいですか?>")
#     if i == "YES" or i == "yes" or i == "はい" or i == "y":
#         print("終了します")
#         break

# import turtle
# t = turtle.Pen()

# while True:
#     i = input("turtle>")
#     if i == "forward":
#         t.forward(100)
#     elif i == "left":
#         t.left(90)
#     elif i == "right":
#         t.right(90)
#     elif i == "turn":
#         t.right(180)
#     elif i == "quit":
#         print("終了します")
#         break

# import random
# value = random.choice(range(0, 100))
# print(value)

# import random
# number = random.choice(range(0, 100))
# while True:
#     value = int(input("数字?>"))
#     if value == number:
#         print("正解です")
#         break
#     elif value < number:
#         print("小さいです")
#     elif value > number:
#         print("大きいです")

# import random
# value = random.choice([1, 2, 3, 4, 4, 5, 5, 3, 3, 3])
# print(value)

import random
number = random.choice(range(0, 100))
c = 0
while True:
    value = int(input("数字?>"))
    c = c + 1
    if value == number:
        print("正解です")
        break
    elif value < number:
        print("小さいです")
    elif value > number:
        print("大きいです")
print(f"入力回数: {c}")
