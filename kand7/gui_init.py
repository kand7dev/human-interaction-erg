from tkinter import *
import tkinter.ttk as ttk
# from tkinter.ttk import *
FOREGROUND = "#c0ae6b"
BACKGROUND = "#2d1d50"
FONT = "monospace"


def createWindow(geo="1000x800"):
    window = Tk()
    window.title("Our Virtual Assistant")
    window.geometry(geo)
    window.configure(background=BACKGROUND)

    welcomeString = Label(text="Welcome to our App", padx=5,
                          pady=35, foreground=FOREGROUND, background=BACKGROUND, font=("Courier New", 25),)
    welcomeString.pack(padx=20, pady=0)
    Label(text="Username", foreground=FOREGROUND,
          background=BACKGROUND, font=FONT).pack(side=TOP, pady=15)
    Entry(width=30, border=2, font=FONT).pack()
    Label(text="Password", foreground=FOREGROUND,
          background=BACKGROUND, font=FONT).pack(pady=15)
    # passLabel.grid(row=4, column=0, padx=50, pady=70)
    Entry(width=30, border=2, font=FONT).pack()
    Button(window, text="Quit", command=quit, pady=5,
           padx=5, font=FONT, background=BACKGROUND, foreground=FOREGROUND, highlightthickness=0, activebackground=FOREGROUND).pack(padx=10, pady=10)
    menuBar = Menu(window)
    menuBar.config(background=FOREGROUND,
                   foreground=BACKGROUND, font=("monospace", 10))
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Functions")
    fileMenu.add_command(label="Help")
    fileMenu.config(background=FOREGROUND,
                    foreground=BACKGROUND, font=("monospace", 10))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit)
    menuBar.add_cascade(label="File", menu=fileMenu)
    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.config(background=FOREGROUND,
                    foreground=BACKGROUND, font=("monospace", 10))
    helpMenu.add_command(label="Help")
    menuBar.add_cascade(label="Help", menu=helpMenu)
    window.config(menu=menuBar)

    return window


window = createWindow()
window.mainloop()
