def list_reverse(i):
    length = len(i)

    for x in range(int(length / 2)):
        tmp1 = i[x]
        tmp2 = i[length - x - 1]

        i[x] = tmp2
        i[length - x - 1] = tmp1

        x = x + 1
    return i


a = input("リストを入力")
values = eval(a)
result = list_reverse(values)
print(result)
