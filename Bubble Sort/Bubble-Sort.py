import random as r
'''Firstly we decided to how are we gonna build our list'''
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

'''We created our list properly, now lets sort it by Bubble Sort Algorithm'''
'''Bubble sort algorithm starts from last element of an array and compares every element with previous until the first element of that 
array, while comparing, if first element is smaller than second one, algorithm switches them. 
After de last switch, array will be all sorted. This algorithm's complexity is O(n^2). '''

def BubbleSort(list):
    flag = 1
    '''This flag shows us if there is any switches while checking the list'''
    while (flag != len(list)):
        flag=1
        for i in range(len(list)-1,0,-1):
            if list[i]< list[i-1]:
                list[i] , list[i-1] = list[i-1] , list[i]
                print(list)
                flag = 1
            else:
                flag +=1
    

BubbleSort(list) 
print("Final status of the list is --> ", list)
