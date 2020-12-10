# values = [3, -2, 5, 7, -6]
# result = []
# for x in values:
#     result.append(x * 6)
# print(f"結果:{result}")

# r = 0

# with open(r"aaa.txt") as file:

#     for x in file:

#         vs = x.split(",")

#         if vs[0] == "B":

#             r = r + int(vs[1])

#         elif vs[0] == "R":

#             r = r - int(vs[1])

# print(r)


# def filter(numbers, n):
#     result = []
#     for x in numbers:
#         if x < n:
#             result.append(x)
#     return result


# with open(r"iii.txt", encoding="UTF-8") as file:
#     result = 0
#     for i in file:
#         if int(i) > 0:
#             result = result + i
#     print(result)

# import random
# while True:
#     i = input()
#     if i == "go":
#         r = random.random()
#         if r < 0.5:
#             print("表")
#         else:
#             print("裏")
#     elif i == "quit":
#         break

# i = "[[1, 2, 3], [1, 3, 9],[1, 5, 8], [7, 8, 9]]"

# values = eval(i)

# v = values[0]

# n = v[0]
# print(n)

# for x in values:

#     for y in x:

#         if n <= y:

#             v = x

#             n = y

# print(v)

# def check_uru(year):

#     if year % 4 == 0:

#         if year % 100 == 0:

#             if year % 400 == 0:

#                 return 0

#             else:

#                 return 1

#         else:

#             return 0

#     else:

#         return 1


# s_year = 2000
# e_year = 2100


# def uru_years(s_year, e_year):
#     for i in [s_year:e_year]:
#         if check_uru == 0:
#             print(i)


# i = int(input())
# lst = []
# c_two = 0
# c_four = 0
# while i > 0:
#     lst.append(i % 10)
#     i //= 10
#     if i % 10 == 2:
#         c_two = c_two + 1
#     elif i % 10 == 4:
#         c_four = c_four + 1
# if c_two < c_four:
#     print(4)
# else:
#     print(2)


# import turtle
# t = turtle.Pen()
# inputs = ["a.2", "b.3", "a.2", "c.3", "a.2", "C.3", "a.2"]
# values = []
# for x in inputs:
#     o = x.split(".")
#     values.append({"f": o[0], "v": int(o[1])})
#     for x in values:
#         f = x["f"]
#         v = x["v"]
#         if f == "a":
#             t.forward(v * 20)
#         elif f == "b":
#             t.right(v * 30)
#         elif f == "c":
#             t.left(v * 30)

# import turtle
# t = turtle.Pen()
# a = int(input())
# for x in range(20):
#     v = (x + 1) * 10
#     t.forward(v)
#     t.left(a * 30)
