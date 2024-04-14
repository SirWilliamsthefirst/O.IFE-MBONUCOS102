total = 50 #this is global variable.
def sum (arg1,arg2):
    #Add both the parameters
    total = arg1 + arg2
    print("Inside the fuction local total: ",total)
    return total

#Now you can call sum function
sum(10,20)
print("oputside the function global total: ",total)