import random as r
#Firstly we decided to how are we gonna build our list
randomOrNot=int(input("If you want to assign numbers yourself insert '1' to randomize it insert '2': "))
length = int(input("Set list length: "))
list=[]
for i in range(0, length):
    if randomOrNot == 1:
        print(i,". number: ")
        list.append(int(input()))
    else:
        list.append(r.randint(0,1000))
print("Your list is --> " ,list)

def InsertionSort(list):
    max=len(list)-1
    sorted=0
    insertion=sorted+2
    while sorted !=max:
        for i in range(sorted,-1,-1):
            print(list)
            insertion -=1
            if list[insertion]<list[sorted]:
                list[insertion] , list[sorted] = list[sorted] , list[insertion]
                
        sorted+=1
        insertion=sorted+2

InsertionSort(list)
print(list)
    
