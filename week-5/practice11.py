import tkinter as tk
from tkinter import messagebox
#from tkinter import Image,_ImageTk

def welcomeMessage(username):
    #create a tkinter window 
    window = tk.Toplevel(root)
    window.title("Admin Box")
    window.geometry("500x200")

    label_1 = tk.Label(window,text=f"welcome{username}\n")
    label_1.pack()
    label_2 = tk.Label(window,text="this is python GUI with tkinter")
    label_2.pack()

    #Run the tkinter event loop
    root.mainloop()

def submit():
        username = username_entry.get()
        password = password_entry.get()

        if username == "Mary" and password == "cos102":
              welcomeMessage(username)
        else:
              messagebox.showerror("login","invalid user or password")

 #Create main window
root = tk.Tk()
root.title("login form")
root.geometry("500x200")

#Create username Label and entry
username_label = tk.Label(root,text="username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#Create password Label and entry
password_label = tk.Label(root,text="password:")
password_label.pack()
password_entry = tk.Entry(root)
password_entry.pack()

#Create submit button
submit_button = tk.Button(root,text="Submit",command=submit)
submit_button.pack()

#Run the main event loop
root.mainloop()