#!/usr/bin/python3
import random

MERG = 'Merge_Sort.txt'
HEAP = 'Heap_Sort.txt'
INSE = 'Insertion_Sort.txt'
BUBB = 'Bubble_Sort.txt'

#simple function for writing to file
#parameters are filename(look at constants above) and the data to write
def write2file(filename, message):
    myfile = open(filename, 'a')
    myfile.write(message + "\n")
    myfile.close()

#generate a random array
def rand_array(size):
    arr = []
    for i in range(1, size+1):
        a = random.randint(0, 10000000)
        arr.append(a)
    return arr

#generate best case array(sorted in ascending order)
def sorted_array_BEST(size):
    arr = []
    for i in range(1, size+1):
        arr.append(i)
    return arr

#generate worst case array(sorted in descending order)
def sorted_array_WORST(size):
    arr = []
    for i in range(1, size+1):
        arr.append(size - (i-1))
    return arr

test1 = 1234
test2 = 5678
write2file(MERG, str(test1)) 
write2file(MERG, str(test2))

test3 = rand_array(10)
print(test3)

test4 = sorted_array_BEST(10)
print(test4)

test5 = sorted_array_WORST(10)
print(test5)

test6 = sorted_array_WORST(100)
test7 = sorted_array_BEST(100)

def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        insertion_comparison = 0
        
        while pos > 0 and arr[pos - 1] > cursor:
            insertion_comparison+=1
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    print(insertion_comparison)
    write2file(INSE, "This is the number of comparisons for a worst case insertion sort:")
    write2file(INSE, str(insertion_comparison))
    return arr

#This Algorithm Was Obtained From GeeksforGeeks.org 
def heapify(arr, n, i): 
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l
        
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
       
  
        # Heapify the root. 
        heapify(arr, n, largest) 
    
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr)
    heap_comparison = 0
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)
        heap_comparison+=1

insertion_sort(test6)
heapSort(test7)
