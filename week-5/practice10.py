import tkinter as tk

#handling button click event
def button_click():
    #print("button clicked!")
    
    #show on information message box
    msgbox.showinfo("info","welcome to cos 102 GUI App!\n")

    #Ask for user confirmation
    result = msgbox.askyesno("confirmation","do you want continue?")

#Create the main window
root = tk.Tk()
root.title("home page")
root.geometry("100x100")

#Add a label widget
label = tk.Label(root,text="hello friend \n")
label.pack()

#Add a button widget
button = tk.Button(root,text="Click me!",command=button_click)
button.pack()

#Style the button widget
button.config(fg="red",bg="yellow")

#Start the event loop 
root.mainloop()
