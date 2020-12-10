with open(r"register.csv", encoding="UTF-8") as file:
    next(file)
    total = 0
    for i in file:
        sline = i.rstrip("\n")
        sline = sline.split(",")
        price = int(sline[1]) * int(sline[2])
        print(f"{str(sline[0])}の合計: {str(price)}円")
        total = total + price

    print(f"合計金額: {total}円")
