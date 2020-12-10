input_lists = eval(input("リストを入力 >"))

with open(r"07/list.txt", encoding="UTF-8", mode="w") as file:
    for i in input_lists:
        print(i)
        file.write(str(i) + "\n")
