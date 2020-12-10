i = input("リスト>")
values = eval(i)

current = 0
s = 0

for x in values:
    s = s + x
    current = current + 1

print(f"平均値: {s / current}")
