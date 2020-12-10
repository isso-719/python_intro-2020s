from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()


def on_click(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x - 50, y - 50, x + 50, y + 50)


canvas.bind("<Button-1>", on_click)
