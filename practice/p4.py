import tkinter as tk

def food(a,b):

    a = 3
    b = 2
    c = a+b
    return c
root = tk.Tk()

root.title("Food App")

root.geometry("300x400")

label = tk.Label(root,text = food(3,4))

label.pack()

root.mainloop()