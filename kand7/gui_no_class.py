from tkinter import *
from PIL import Image, ImageTk

# from tkinter.ttk import *
FOREGROUND = "#c0ae6b"
BACKGROUND = "#2d1d50"
FONT = "monospace"
WIDTH = 700
HEIGHT = 500


def testCommand():
    print("Hello World!")


def createMenuBar(mainWindow):
    menuBar = Menu(mainWindow)
    menuBar.config(background=BACKGROUND,
                   foreground=FOREGROUND, border=False, font=("monospace", 12))
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Functions", command=testCommand)
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
    mainWindow.config(menu=menuBar)


def createWindow():
    window = Tk()
    window.title("Our Virtual Assistant")
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    x = (screen_width/2) - (WIDTH/2)
    y = (screen_height/2) - (HEIGHT/2)
    window.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, 0))

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

    return window


def createAnimationWindow():
    newWindow = Toplevel(bg=BACKGROUND)
    newWindow.geometry("%dx%d+%d+%d" %
                       (WIDTH, HEIGHT, WIDTH, 0))
    animation_frame = Frame(newWindow)
    images = []
    for i in range(1, 335):
        image_path = f'/home/kand7/Desktop/Repos/personal_assistant/images/new_name_{i}.png'
        image = Image.open(image_path).convert('RGBA')
        images.append(ImageTk.PhotoImage(image))
    animation_label = Label(
        animation_frame, image=images[0], bg='black')
    animation_label.pack()
    animation_frame.pack(fill='both', expand=True)
    current_image = 0
    for i in range(len(images)):
        animation_label.config(image=images[i])
        current_image = (current_image + 1) % len(images)


window = createWindow()
createMenuBar(window)
createAnimationWindow()
window.mainloop()
