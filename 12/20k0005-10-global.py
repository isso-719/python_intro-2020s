from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=300)
canvas.pack()

x = 0
y = 0


def on_click(event):
    global x
    global y
    tmp_x = event.x
    tmp_y = event.y

    canvas.create_line(tmp_x, tmp_y, x, y)

    x = tmp_x
    y = tmp_y


canvas.bind("<Button-1>", on_click)
