from tkinter import *
from tkinter import simpledialog

#Create login window
def login_window():
    login = Tk()
    login.title("Virtual Personal Assistant - Login")
    login.geometry("300x200")
    login.configure(bg="#6B8E23")
    #Create login function
    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        #Check if the credentials are correct
        if username == "admin" and password == "admin":
            login_success["value"] = True
            login.destroy()
        else:
            error_label.config(text="Incorrect username or password")
    #Add widgets to login window
    Label(login, text="Username:", font=("Roboto", 12), bg="#6B8E23").place(x=50, y=50)
    Label(login, text="Password:", font=("Roboto", 12), bg="#6B8E23").place(x=50, y=90)
    username_entry = Entry(login)
    username_entry.place(x=150, y=50)
    password_entry = Entry(login, show="*")
    password_entry.place(x=150, y=90)
    Button(login, text="Login", font=("Roboto", 12), bg="#98FB98", command=login_action).place(x=130, y=130)
    error_label = Label(login, text="", font=("Roboto", 12), fg="red", bg="#6B8E23")
    error_label.place(x=50, y=160)
   
    #Run login window
    login.mainloop()

login_success = {"value": False}
login_window()

if login_success["value"]:
    #Create main window
    main = Tk()
    main.title("Virtual Personal Assistant")
    main.geometry("500x300")
    main.configure(bg="#98FB98")

    #Add menu bar to main window
    menubar = Menu(main)

    #Create File submenu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Functions")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=main.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    #Create View submenu
    view_menu = Menu(menubar, tearoff=0)
    view_menu.add_command(label="Zoom In")
    view_menu.add_command(label="Zoom Out")
    view_menu.add_command(label="Full Screen")
    menubar.add_cascade(label="View", menu=view_menu)

    #Create Help submenu
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="User Manual")
    help_menu.add_command(label="About")
    menubar.add_cascade(label="Help", menu=help_menu)

    main.config(menu=menubar)
    #Add label and entry for user input
    Label(main, text="What can I help you with?", font=("Roboto", 16), bg="#98FB98").place(x=50, y=50)
    user_input_box = Entry(main, font=("Roboto", 16), width=30)
    user_input_box.place(x=50, y=100)

    #Add label to display messages
    message = Label(main, text="", font=("Roboto", 16), bg=main.cget('bg'))
    message.place(x=50, y=150)

    #Define function to handle user input
def search_action():
    user_input = user_input_box.get()
    if user_input:
        message_label = Label (main, text="I will search for " + user_input, font=("Roboto", 16), bg="#98FB98", anchor='w')
        message_label.place(x=50, y=50)
        message.config(text="")
        message.after(1, message.config, {"text": ""}) # clear message after 3 seconds
        user_input_box.delete(0, END)
    else:
        message.config(text="Please enter something to search for.")

submit_button = Button(main, text="Submit", font=("Roboto", 16), bg="#6B8E23", fg="white", command=search_action)
submit_button.place(relx=0.5, rely=0.5, anchor=CENTER, y=50, width=100, height=50)

#Run main window
main.mainloop()
