def changeme(mylist):
    #This changes a passed list
    mylist.append([1,2,3,4])
    print("Value inside the function: ",mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print("value outside the function: ",mylist)