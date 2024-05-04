import tkinter as tk

root = tk.Tk()

root.title("my GUI App")

root.geometry("300x400")

label = tk.Label(root,text = "hello,GUI!")

label.pack()

root.mainloop()