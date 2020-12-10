with open(r"07/example.txt", encoding="UTF-8") as file:
    for line in file:
        sline = line.rstrip("\n")
        print(f"行: {sline}")
