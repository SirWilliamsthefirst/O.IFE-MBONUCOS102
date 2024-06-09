print("for girls")

name = ['evely','jessica','somto','edith','lizza','mandona','wojo','tola','aisha','latifa']
age = [17,16,17,18,16,18,17,20,19,17]
height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
scores = [80,85,70,60,76,66,87,95,50,49]

for i in range(0,10):
    print(i,name[i],age[i],height[1],scores[i])
 
print("\nfor boys")

name = ['chinedu','liam','wale','Gbenga','abiola','kola','kunle','george','thomas','wasley']
age = [17,16,17,18,20,19,16,18,17,19]
height = [5.7,5.9,5.8,5.5,6.1,5.5,6.1,6.0,5.7,5.5]
scores = [80,85,70,60,76,66,87,95,50,49]

for i in range(0,10):
    print(f'{name[i]} | {age[i]} | {height[1]} | {scores[i]}')


def printinfo(arg1,*tuple):
    #This is test
    print("output is: ")
    print(arg1)
    for var in tuple:
        print(var)
        return
printinfo(10)
printinfo(70,60,50)        