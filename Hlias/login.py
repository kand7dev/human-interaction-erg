from tkinter import *
import os


def register_user():
  global username_info
  global password_info

  username_info = username.get()
  password_info = password.get()

  file=open(username_info+".txt", "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0, END)
  password_entry.delete(0, END)

  Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x250")
  
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()

  Label(screen1, text = "Please enter details below").pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username * ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()


def login_user():
  if os.path.exists(username_info and password_info):
    Label(screen2, text = "login Sucess", fg = "green" ,font = ("calibri", 11)).pack()
  else:
    Label(screen2, text = "Login failed", fg = "green" ,font = ("calibri", 11)).pack()


def login():
  global screen2

  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("300x250")
  username = StringVar()
  password = StringVar()

  Label(screen2, text = "Please enter details below").pack()
  Label(screen2, text = "").pack()
  Label(screen2, text = "Username ").pack()
  username_entry = Entry(screen2, textvariable = username)
  username_entry.pack()
  Label(screen2, text = "Password * ").pack()
  password_entry =  Entry(screen2, textvariable = password)
  password_entry.pack()
  Button(screen2, text = "login", width = 10, height = 1, command = login_user).pack()
  



def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x250")
  screen.title("Notes 1.0")
  screen.configure(bg='orange')
  Label(text = "Notes 1.0", bg = "orange", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "", bg = "orange").pack()
  Button(text = "Login", bg='white', height = "2", width = "30", command = login).pack()
  Label(text = "", bg = "orange").pack()
  Button(text = "Register",bg='white',height = "2", width = "30", command = register).pack()

  screen.mainloop()

main_screen()