# Question1
def map_square(v):
    result = []
    for x in v:
        y = x ** 2
        result.append(y)
    return result


v = [1, 2, -1, -2]
print("問題1")
print(map_square(v))


# Question2
def filter_positive(v):
    result = []
    for x in v:
        if x > 0:
            result.append(x)
    return result


v = [1, 2, -1, -2]
print("問題2")
print(filter_positive(v))


# Question3
def sum_square(values):
    result = 0
    for x in values:
        result = result + x ** 2
    return result


values = [1, -2, 3, -4, 5]
result = sum_square(values)
print("問題3")
print(f"result = {result}")


# Question4
def sum_positive(values):
    result = 0
    for x in values:
        if x > 0:
            result = result + x
    return result


values = [1, -2, 3, -4, 5]
result = sum_positive(values)
print("問題4")
print(f"result = {result}")
