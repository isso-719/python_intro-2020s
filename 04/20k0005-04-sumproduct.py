i = input("値段>")
j = input("量>")

val = eval(i)
qty = eval(j)

current = 0

for x in val:
    k = val[current] * qty[current]
    print(f"リスト{current}番同士の結果: {k}")
    current = current + 1
