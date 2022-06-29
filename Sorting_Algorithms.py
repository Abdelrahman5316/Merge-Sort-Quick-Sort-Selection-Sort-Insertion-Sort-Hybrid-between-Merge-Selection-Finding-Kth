import sys
import time
import copy
import random
def merges(Arr,left,right):
    if(left<right):
     mid=(left+right)//2
     merges(Arr,left,mid)
     merges(Arr,mid+1,right)
     merge(Arr,left,mid,right)
def hybrid(Arr,left,right,threshold):
    
    if((right-left+1) > threshold):
        #print(right-left)
        if(left<right):
         mid=(left+right)//2
         hybrid(Arr,left,mid,threshold)
         hybrid(Arr,mid+1,right,threshold)
         merge(Arr,left,mid,right)
    else:
        #print(right-left+1)
        selectionsort(Arr)
def merge(Arr,left,mid,right):
    Ll=mid-left+1
    Lr=right-mid
    L=[]
    
    R=[]
    for i in range(0,Ll):
        L.append(Arr[left+i])
        
    for i in range(0,Lr):
        R.append(Arr[mid+1+i])
    x=0
    y=0
    z=left
    while(x<Ll and y<Lr):
        if(L[x]<=R[y]):
            Arr[z]=L[x]
            x+=1
            z+=1
        else:
            Arr[z]=R[y]
            y+=1
            z+=1
    while(x<Ll):
        Arr[z]=L[x]
        x+=1
        z+=1
    while(y<Lr):
        Arr[z]=R[y]
        y+=1
        z+=1
def selectionsort(Arr):
    
    for i in range(0,len(Arr)-1):
        mn=i
        for j in range(i+1,len(Arr)):
            if(Arr[j]<Arr[mn]):
                mn=j
        if(i != mn):
            Arr[i],Arr[mn]=Arr[mn],Arr[i]
    return Arr
def insertionsort(Arr):
    for i in range(1,len(Arr)):
        key=Arr[i]
        j=i-1
        while(j>=0 and Arr[j]>key):
            Arr[j+1]=Arr[j]
            j=j-1
        Arr[j+1]=key
    return Arr



def quick_sort(Arr,first,last):
    if(first<last):
        piv=randompart(Arr,first,last)
        quick_sort(Arr,first,piv-1)
        quick_sort(Arr,piv+1,last)





def randompart(Arr,first,last):
    indx= random.randint(first,last)
    Arr[indx], Arr[last]=Arr[last],Arr[indx]
    return partition(Arr,first,last)


def partition(Arr,first,last):
    pivot=Arr[last]
    i=(first-1)
    for j in range(first,last):
        if(Arr[j]<pivot):
            i=i+1
            Arr[i],Arr[j]=Arr[j],Arr[i]
    Arr[i+1],Arr[last]=Arr[last],Arr[i+1]
    return (i+1)




def getksmallestelement(A,first,last,k):
    if(k>0 and k<=len(A)):    #lenght of array is =(last-first+1)

        pivot=partition(A,first,last)

        if(pivot-first==k-1):
            return A[pivot]

        if(pivot-first>k-1):
            return getksmallestelement(A,first,pivot-1,k)

        if(pivot-first<k-1):   #k=k-1
            return getksmallestelement(A,pivot+1,last,k-pivot+first-1)   #-(pivot-first+1)
    else: print("the k entered is invalid")


Arr=input("Enter array to sort\n")
Arr2=[]
Arr3=[]

z=100
while z>50:
    Arr2.append(z)
    z-=1
Arr=Arr.split()
Arr=list(map(int,Arr))
Arr3=copy.deepcopy(Arr)
sys.setrecursionlimit(2000)
while True:
    
    print("\n")
    opt=input("Enter 0:Exit 1:selection 2:insertion 3:merge 4:hybrid 5:quick 6:smallestkthelement 7:Result\n")
    if opt=="1":
        Arr=copy.deepcopy(Arr3)
        begin = time.time()
        print("Selection sort: {}".format(selectionsort(Arr)))
        end = time.time()
        print("Total runtime of the program is {}".format(end-begin))
    elif opt=="2":
        Arr=copy.deepcopy(Arr3)
        begin = time.time()
        print("insertion sort: {}".format(insertionsort(Arr)))
        end = time.time()
        print(f"Total runtime of the program is {end - begin}")
    elif opt=="3":
        
        Arr=copy.deepcopy(Arr3)
        print(Arr3)
        begin = time.time()
        merges(Arr,0,len(Arr)-1)
        print("Merge sort: {}".format(Arr))
        end = time.time()
        print(f"Total runtime of the program is {end - begin}")
    elif opt=="4":
        #Arr=copy.deepcopy(Arr3)
        x=int(input("Enter the threshold for hybrid\n"))
        begin = time.time()
        hybrid(Arr2,0,len(Arr2)-1,x)
        print("Hybrid sort for 50 elements array:{}".format(Arr2))
        end = time.time()
        print(f"Total runtime of the program is {end - begin}")
        #print("Hybrid sort for input array:{}".format(Arr))
    elif opt=="5":
        Arr = copy.deepcopy(Arr3)
        print(Arr)
        begin = time.time()
        quick_sort(Arr, 0, len(Arr) - 1)
        print("quick sort: {}".format(Arr))
        end = time.time()
        print(f"Total runtime of the program is {end - begin}")


    elif opt=="6":
        k = int(input("Enter value of k: "))
        Arr = copy.deepcopy(Arr3)
        begin = time.time()
        index = getksmallestelement(Arr, 0, len(Arr) - 1, k)
        print("the smallest ", k, "th element is:", index)
        end = time.time()
        print(f"Total runtime of the program is {end - begin}")
    elif opt=="7":
        print("Unsorted: {}".format(Arr3))
        print("Sorted:{}".format(Arr))
    elif opt=="0":
     break
