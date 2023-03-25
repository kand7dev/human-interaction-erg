from tkinter import *
from tkinter.ttk import *


def createWindow(geo="1000x800"):
    window = Tk()
    window.title("Our Virtual Assistant")
    window.geometry(geo)
    Label(text="Quit Button").pack()
    Button(window, text="Quit", command=quit).pack()
    return window


window = createWindow()
Label(text="Creating new Labels", foreground="white", background="black").pack()
window.mainloop()
