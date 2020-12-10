import turtle

t = turtle.Pen()

with open(r"turtle.txt", encoding="UTF-8") as file:
    for i in file:
        sline = i.rstrip("\n")
        sline = sline.split(":")

        if sline[0] == "FORWARD":
            t.forward(int(sline[1]))
        elif sline[0] == "LEFT":
            t.left(int(sline[1]))
        elif sline[0] == "RIGHT":
            t.right(int(sline[1]))
