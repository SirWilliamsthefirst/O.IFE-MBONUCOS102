import tkinter as tk

def food():
    username = input("Username")
    password = "Lsryy"
    return username,password
def submit():
    output = tk.Label(root,text = f"Hello {entry.get()}")
    output.pack()
root = tk.Tk()

root.title("Food App")

root.geometry("300x400")


label = tk.Label(root,text = "Enter Name")
label.pack()
entry = tk.Entry(root)
entry.pack()

sub = tk.Button(root,text = "Submit", command = submit).pack()



root.mainloop()