def find(a, b):
    current = 0
    for x in values:
        if x == b:
            return current
        current = current + 1
    return -1


i = input("リストを入力")
values = eval(i)
index = find(values, 100)

if index == -1:
    print("100は一つも含まれない")
else:
    print(f"100は{index}番目に含まれる")
