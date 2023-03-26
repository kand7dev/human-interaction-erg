from tkinter import *
from PIL import Image, ImageTk


class myGUI:

    def __init__(self, foreground=None, background=None):

        # We can give parameters to change window colors at the constructor
        # initializing fonts-colors-titles
        if (foreground == None and background == None):
            self.foreground = "#c0ae6b"
            self.background = "#2d1d50"
        else:
            self.foreground = foreground
            self.background = background
        self.font = "monospace"
        self.width = 700
        self.height = 500
        self.window = Tk()
        self.window.title("Our Virtual Assistant")
        self.window.geometry("%dx%d+%d+%d" % (self.width, self.height, 0, 0))

        self.window.configure(background=self.background)

        # Header
        self.welcomeString = Label(text="Welcome to our App", padx=5,
                                   pady=35, foreground=self.foreground, background=self.background, font=("Courier New", 25),)
        self.welcomeString.pack(padx=20, pady=0)

        # Username prompt
        self.username = Label(text="Username", foreground=self.foreground,
                              background=self.background, font=self.font)
        self.username.pack(side=TOP, pady=15)
        self.username_entry = Entry(width=30, border=2, font=self.font)
        self.username_entry.pack()

        # Password prompt
        self.password = Label(text="Password", foreground=self.foreground,
                              background=self.background, font=self.font)
        self.password.pack()
        self.password_entry = Entry(width=30, border=2, font=self.font)
        self.password_entry.pack()

        # Quit button
        self.quit_button = Button(self.window, text="Quit", command=self.window.destroy, pady=5,
                                  padx=5, font=self.font, background=self.background, foreground=self.foreground, highlightthickness=0, activebackground=self.foreground)
        self.quit_button.pack(padx=10, pady=10)

        # Header Menu
        self.menuBar = Menu(self.window)
        self.menuBar.config(background=self.background,
                            foreground=self.foreground, border=False, font=("monospace", 12))
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="Functions")
        self.fileMenu.add_command(label="Help")
        self.fileMenu.config(background=self.foreground,
                             foreground=self.background, font=("monospace", 10))
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.window.destroy)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.helpMenu = Menu(self.menuBar, tearoff=0)
        self.helpMenu.config(background=self.foreground,
                             foreground=self.background, font=("monospace", 10))
        self.helpMenu.add_command(label="Help")
        self.menuBar.add_cascade(label="Help", menu=self.helpMenu)
        self.window.config(menu=self.menuBar)

        # Second Animating Window
        self.animationWindow = Toplevel()
        self.animationWindow.geometry("%dx%d+%d+%d" %
                                      (self.width, self.height, self.width, 0))
        self.animation_frame = Frame(self.animationWindow)
        self.images = []
        for i in range(1, 335):
            image_path = f'/home/kand7/Desktop/Repos/personal_assistant/images/new_name_{i}.png'
            image = Image.open(image_path).convert('RGBA')
            self.images.append(ImageTk.PhotoImage(image))
        self.animation_label = Label(
            self.animation_frame, image=self.images[0], bg='black')
        self.animation_label.pack()
        self.animation_frame.pack(fill='both', expand=True)
        self.current_image = 0
        self.animate()
    # Loop for events
        self.window.mainloop()

    def animate(self):
        self.animation_label.config(image=self.images[self.current_image])
        self.current_image = (self.current_image + 1) % len(self.images)
        self.window.after(20, self.animate)


app2 = myGUI()
