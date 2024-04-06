name = input("Enter your name:")
age = int(input("EAnter your age:"))
yoe = int(input("Enter your years of experience:"))

if yoe > 25 and age >= 55:
    print("Your annual tax revenue is N5600000")

elif yoe > 20 and age >= 45:
    print("Your annual tax revenue is N4480000")

elif yoe > 10 and age >= 35:
    print("Your annual tax revenue is N1500000")

elif yoe > 10 and age < 35:
    print("Your annual tax revenue is N550000")

else:
    print("Invalid input.")