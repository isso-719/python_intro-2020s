form = input("検索>")
triger = False

with open(r"dic.txt", encoding="UTF-8") as file:
    for i in file:
        sline = i.split(":")

        if sline[0] == form:
            result = sline[1].rstrip("\n")
            print(f"{form}:{result}")
            triger = True

if triger == False:
    print(f"{form}は辞書にありません")
