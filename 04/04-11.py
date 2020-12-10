i = input("リスト>")
values = eval(i)

current = values[0]

for x in values:
    if x > current:
        current = x

print(f"最大値: {current}")
