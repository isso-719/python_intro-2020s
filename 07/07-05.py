with open(r"07/numbers.txt") as file:
    current = 0
    summary = 0
    for line in file:
        summary = summary + float(line)
        current = current + 1
    aver = summary / current
    print(f"平均値: {aver}")
    print(f"{summary}, {current}")
