with open(r"07/target.txt", encoding="UTF-8", mode="w") as file:
    file.write("Hello world! 日本語\n")
    file.write(str(100) + "\n")
    file.write(f"数値: {100}")
