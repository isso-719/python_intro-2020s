def has_negative(values):
    current = 0
    for x in values:
        if values[current] < 0:
            return True
        current = current + 1


i = input("リストを入力")
values = eval(i)

if has_negative(values):
    print("負の値が含まれる")
else:
    print("負の値は含まれていない")
