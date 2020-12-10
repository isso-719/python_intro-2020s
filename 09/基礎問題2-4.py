values = ["10,20,30", "40,50,60", "70,80,90"]

queue = []
for i in values:
    sline = i.split(",")

    result = 0
    for j in sline:
        result = result + int(j)

    queue.append(result)


with open(r"09/result2.txt", encoding="UTF-8", mode="w") as result:
    result.write(str(queue))
