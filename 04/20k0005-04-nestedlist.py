i = input("値を入力>")

j = eval(i)

current = 0
count = 0
result = 0

for x in j:

    for y in x:
        if y > current:
            current = y

    if current > result:
        result = current

    count = count + 1

print("結果は以下の通りです。")

for x in j:

    if result in x:
        print(x)
