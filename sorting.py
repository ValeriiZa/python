#!/usr/local/bin/python3
import time, sys
#from datetime import now
from datetime import datetime

#print (sys.version)
#print (sys.version_info)
#print (sys.version_info[0])
#time.sleep(10)

##################################################
#################   Bubble    ####################
def bubble (arr, ascendance):
    # Check of put parameter
    if type(arr) != list or type(ascendance) != bool:
        print ( "You enter {} as the first parameter.".format(type(arr).__name__) )
        #print (f"You enter { str(type(arr).__name__) } as the first parameter." )
        return 0
    elif type(arr) == list:
        for el in arr:
            temp = type(el).__name__
            if temp != 'int' and temp != 'float':
                print ("not a number into list")
                return 1
            elif len (arr) == 1:
                return arr
        print ("Is fine!")
    # Sort
    t = datetime.now()
    for i in range( len(arr)-1, -1, -1 ):
        for j in range (0, i):
            if (ascendance):
                if arr[j]>arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
            else:
                if arr[j]<arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
                #print (i, j, arr)
    print ("bubble asc=", ascendance, datetime.now()-t)

def bubble_asc (arr):
    bubble (arr, True)

def bubble_desc (arr):
    bubble (arr, False)

##################################################
###################   selection   ################
def selection (arr):
    t = datetime.now()
    arr_size = len(arr)
    for i in range(0, arr_size):
        min = i
        for j in range (i, arr_size):
            if arr[j] < arr[min] :
                min = j
        if min != i:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
        #print (arr)
    print ("Selection t:", datetime.now()-t)
    
##################################################
###################   Insertion   ################
def insertion (arr):
    t = datetime.now()
    arr_size = len(arr)
    for i in range (1, arr_size):
        j=i-1
        while ( arr[j]>arr[j+1] and j>=0 ):
            temp = arr[j]
            arr[j]=arr[j+1]
            arr[j+1] = temp
            j=j-1
        print (arr)
    print ("Insertion t:", datetime.now()-t)

def swap (arr, n, m):
    temp = arr[n]
    arr[n] = arr[m]
    arr[m] = temp
    return arr

def split (arr):
    if( len(arr)>=2 ):
        split( arr[:len(arr)//2] )
        split( arr[len(arr)//2:] )
        
    elif( len(arr)==2 ):
        if( arr[0]>arr[1] ):
            arr = swap (arr, 0, 1)
            
##################################################
######### Merge sort Start #########
def joinArr (a, left, mid, right):
    # 1. count lenth of each part;
    len1 = mid - left + 1
    len2 = right - mid
    # 2. make 2 arr with lenth of each part;
    arrleft = [0]*len1
    arrright = [0]*len2
    # 3. copy parts to temp arr;
    for i in range(len1):
        arrleft[i] = a[left + i]
    for j in range(len2):
        arrright[j] = a[mid + 1 + j]

    # 4. loop thought both temp arr from start at one time
    #    and put at begin smaller element and increment that element.
    i = 0
    j = 0
    k = left
    while i < len1 and j < len2:
        if arrleft[i] < arrright[j]:
            a[left + i + j] = arrleft[i]
            i += 1
        else:
            a[left + i + j] = arrright[j]
            j += 1
        k += 1

    while (i < len1):
        a[k] = arrleft[i]
        i += 1
        k += 1
        
    while (j < len2):
        a[k] = arrright[j]
        j += 1
        k += 1

    return a

def mergeArr (a, left, right):
    if (right > left):
        mid = (right + left)//2
        mergeArr (a, left, mid)
        mergeArr (a, mid+1, right)
        return joinArr (a, left, mid, right)

def merge (arr):
    return mergeArr (arr, 0, len(arr)-1)

######### Merge sort End #########



#######  Quick Sort #######
arr = [3, 2,  1, 7,  4, 0,  6, 8, 3]
def sort ( arr, start=0, finish=None ):
    # 1. Select an element from the array as the pivot (at center).
    if finish == None:
        finish = len(arr)-1
    
    pivot = (start + finish)//2
    # 2. Move smaller to the left, bigger to the right part.
    l = []
    r = []
    middle = arr[pivot]
    print ("_________ arr:", arr)
    print ("___> start + finish", start, finish)
    print ("pivot, arr[pivot]", pivot, arr[pivot])
    for i in range(start, finish+1):
        if i == pivot:
            continue
        elif arr[i] <= arr[pivot]:
            l.append(arr[i])
        else:
            r.append(arr[i])
    print ("L: ", l)
    print ("R: ", r)
    print ("arr[pivot]: ", middle)
    for i in range (len(l)):
        arr[ start+i ] = l[i]
    arr[ start+len(l) ] = middle
    for i in range (len(r)):
        arr[ start + len(l) + 1 + i ] = r[ i ]

# 3. Recursively apply the same process to the two partitioned sub-arrays.
# 4. The recursion stops when there is only one element left in the sub-array,
#    as a single element is already sorted.
    if ( len(l)>1 ) :
        sort (arr, start, len(l)-1)
    print ("pivot+1 < finish)", pivot+1, finish, "\n----------\n")
    if (len(r) > 1):
        sort (arr, len(l)+2, finish)
    return arr

###########################

#######  Heap Sort  #######
###########################

#######  Cycle Sort #######
###########################

arr = [3, 2,  1, 7,  4, 0,  6, 8, 3]
##print (merge (arr))
print ("Arr before using SORT method: ", arr)
print ("Arr after using SORT method: ", sort (arr) )

arr = [123, 1, 23, -32]
arr1 = [123,1,23,-32,123,3,-534,64,63,9,12,5,19,11,63,23,1,5,82,9,43,123,44,33,2,1,0,-2]
               
#bubble_asc  (arr1)
#bubble_desc (arr1)

#selection (arr1)
#insertion (arr1)
