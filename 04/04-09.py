i = input("リスト>")
arrays = eval(i)

for x in arrays:
    if x < 10:
        print("OK")
    else:
        print("NG")
