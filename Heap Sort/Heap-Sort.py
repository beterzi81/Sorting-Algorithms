import random as r
import math as m
'''We import math because we need to use math.floor() method later'''
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

'''First we define our branch index finding functions'''

'''This will give us left child of our current heap'''
def Left(i):
    return 2*(i+1)+1
'''This will give us right child of our current heap'''
def Right(i):
    return 2*(i+1)

'''This function will apply heap sorting algorithm to our list'''
def Heapify(list,i):
    largest = 0

    
    '''We keeping the left and right child of our current heap '''
    le = Left(i)
    
    ri = Right(i)
    '''We are checking if left child is bigger than parent'''
    if (le <= heapSize) and (list[le]>list[i]):
        largest = le
        '''If child is bigger, then we assign left child as largest'''
    else:
        largest = i
    '''Then we check the right child if it is bigger than parent'''
    if (ri <= heapSize) and (list[ri]>list[i]):
        largest = ri
    
    if (largest != i):
        '''We making the arrangements'''
        list[i] , list[largest] = list[largest] , list[i]
        '''If there is a swap, we should be sure there is no need to swap anymore. We use Heapify again for largest element.'''
        Heapify(list,largest)
    
    

'''This function will convert our list to heap tree'''

def BuildHeap (list):
    
    for i in range(0,m.floor(len(list)/2)):
        Heapify(list,i)

def HeapSort(list):
    heapSize = len(list)-1
    BuildHeap(list)
    for i in range(len(list)-1,-1,-1):
        list[i] , list[0] = list[0] , list[i]
        heapSize-=1
        Heapify(list,0)



print(list)
    
