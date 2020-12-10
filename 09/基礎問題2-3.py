values = [10, 20, 30]

current = 0
for i in values:
    if current == 0:
        queue = str(i)

    else:
        queue = queue + "\n" + str(i)

    current = current + 1

with open(r"09/result.txt", encoding="UTF-8", mode="w") as result:
    result.write(queue)
