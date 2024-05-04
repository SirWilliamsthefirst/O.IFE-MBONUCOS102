import tkinter as tk
#dictionary for menu with their prices 
menu_items = {
    "Jollof Rice": 350,
    "Coconut Fried Rice": 350,
    "Jollof Spaghetti": 350,
    "Savoury Beans": 350,
    "Roasted Sweet Potatoes": 300,
    "Fried Plantains": 150,
    "Mixed Vegetable Salad": 150,
    "Boiled Yam": 150,
    "Eba": 100,
    "Poundo Yam": 100,
    "Semo": 100,
    "Atama Soup": 450,
    "Eguasi Soup": 450,
    "Sweet Chilli Chicken": 1300,
    "Grilled Chicken Wings": 400,
    "Fried Beef": 400,
    "Fried Fish": 300,
    "Boiled Egg": 200,
    "Sauteed Sausages": 200,
    "Water": 200,
    "Glass Drink": 150,
    "Pet Drink (35cl)": 300,
    "PET Drink (35cl)": 350,
    "PET Drink (30cl)": 500,
    "Glasscanned Malt": 600,
    "Fresh Yo": 350,
    "Pineapple Juice": 350,
    "Mango Juice": 350,
    "Zobo Drink": 350
}     
#to create the windows
root = tk.Tk()
#to create the title
root.title("PAU Cafe")
#to give the widows box size
root.geometry("500x500")
#an array to store all the enties
entry_objects = []
# a dictionary to store the name of the food ordered and the quantity
entries ={}
#to set the positions
y = 0
x=1
#to print the menu out
for key,value in menu_items.items():
    label = tk.Label(root,text=f"{key}, {value}",font=10)
    label.place(x=x,y=y)
    entry = tk.Entry(root)
    entry.insert(0,"0")
    entry.place(x= x+300,y=y,width = 25)
    entry_objects.append(entry)
    y += 50
    if y > 400:
        y =0
        x += 400

#display order, name and discount
def display_information(cost,discount_applied):
    window = tk.Tk()
    window.title("Order Receipt")
    window.geometry("500x500")
    order = ""
    name = name_entry.get()
    _ = tk.Label(window,text = f"Receipt for {name}:", font=('Papyrus',40,'bold')).pack()
    for food_name,quantity_ordered in entries.items():#adds food name and quantity ordered to menu
        if quantity_ordered != '0':
            order += f"{food_name} {quantity_ordered} portions"
            order += "\n"
    order = tk.Label(window, text = order,font = ('Jokerman',20,'italic'),justify="left").pack()
    cost = tk.Label(window, text=f"Amount Due:₦{cost}",font = ('Papyrus',30,'bold')).pack()
    if discount_applied > 0:
        discount = tk.Label(window, text=f"Discount of {discount_applied}% applied!", font =('Vivaldi',30,'bold')).pack()
    window.mainloop()
def tod():
    index = 0
    #gets the food that was ordered and the quantity the user entered
    for key,_ in menu_items.items():
        entries.update({key:entry_objects[index].get()})
        index+=1
    cost()
#calculates the cost and discount
def cost():
    cost = 0
    for food,quantity in entries.items():
        cost += int(quantity) * int(menu_items[food])
        discount = 0
    if cost > 5000:
        cost = cost * 0.75
        discount = 25
    elif cost > 2500:
        cost = cost * 0.85
        discount = 15
    elif cost > 1000:
        cost = cost * 0.90
        discount = 10
    display_information(cost,discount)
button = tk.Button(root,text="submit",command= tod)#once the submit botton is pressed it calls the tod function
button.place(x=700,y=600)
name_label = tk.Label(root,text = "Enter Your Name Here",font = 11).place(x=200,y=600)#label to enter username
name_entry = tk.Entry(root)
name_entry.place(x=440,y=605)
_ = tk.Label(root,text = "THE CAF'S MENU", font = ('Algerian',40,'bold')).place(x=900,y=550)
root.mainloop()