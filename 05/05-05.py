def mysum(i):
    total = 0

    for x in i:
        total = total + x

    return total


values = [10, 20, 30]
result = mysum(values)

print(result)
