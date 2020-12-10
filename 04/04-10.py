i = input("リスト>")
values = eval(i)

current = 0

for x in values:
    print(f"ここまでの値={current}")
    print(f"リストの要素={x}")
    current = current + x

print(f"合計: {current}")
