# e.g "2015/4/1"
line = input("日付入力>")
fields = line.split("/")

print(f"{fields[0]}年{fields[1]}月{fields[2]}日")
