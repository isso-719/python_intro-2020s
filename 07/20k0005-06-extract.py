with open(r"06-extract-in.csv", encoding="UTF-8") as file:
    for x in range(5):
        next(file)

    queue = "年月日,平均気温(°C)\n"
    for i in file:
        sline = i.rstrip("\n")
        sline = sline.split(",")
        queue = queue + str(sline[0]) + "," + str(sline[1]) + "\n"
    queue = queue.rstrip("\n")

    with open(r"result.txt", encoding="UTF-8", mode="w") as result:
        result.write(queue)
    print("ファイルの出力が完了しました")
