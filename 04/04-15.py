i = input("リスト>")
values = eval(i)

current = values[0]

for x in values:
    if current > x:
        current = x

print(f"最小値: {current}")
