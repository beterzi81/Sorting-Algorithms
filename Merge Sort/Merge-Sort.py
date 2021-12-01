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

#This sorting method, split in half every iteration until list length is 1. Then it starts to compare and sort every 2 list again and unites them. In the end, list will be sorted.

def MergeSort (list):
    
    if len(list)>1:
        split = len(list)//2
        #We splitted list until our list length is 1
        left = list[:split]
        right = list[split:]
        
        MergeSort(left)
        MergeSort(right)
        #We assigned iterators for left and right lists 
        i=0
        j=0
        #k variable for main list iterator
        k=0
        #While iterators are not out of range
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                #If left lists i index is lower than right lists j index
                list[k] = left[i]
                #Assign main lists k index as left lists i index value
                i+=1
            else:
                list[k]=right[j]
                #In other case, means right lists j index is lower than left's i index so we assign it
                j+=1
            k+=1
        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1


MergeSort(list)
print(list)

