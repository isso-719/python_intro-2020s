import math

i = input("リストを入力")
numbers = eval(i)


# 平均値を返す関数
def aver(a):
    return sum(a) / len(a)


# 標準偏差を返す関数
def sd(b):
    average = aver(b)
    err = 0
    for x in b:
        err = err + (x - average) ** 2

    dispersion = err / len(b)

    return math.sqrt(dispersion)


print(sd(numbers))
