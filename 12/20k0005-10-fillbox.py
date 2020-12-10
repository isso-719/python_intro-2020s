from tkinter import *

tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="red")
color = "red"


def on_click(event):
    global color

    if ((event.x - 200) ** 2 + (event.y - 200) ** 2) >= 100 ** 2:
        return

    if color == "red":
        canvas.delete("all")
        canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="green")
        color = "green"
    elif color == "green":
        canvas.delete("all")
        canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="blue")
        color = "blue"
    elif color == "blue":
        canvas.delete("all")
        canvas.create_arc(100, 100, 300, 300, extent=359, style=CHORD, fill="red")
        color = "red"


canvas.bind("<Button-1>", on_click)
