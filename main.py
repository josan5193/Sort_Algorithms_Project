#!/usr/bin/python3
import random
from timeit import default_timer as timer
MERG = 'Our_Data/Merge_Sort.txt'
HEAP = 'Our_Data/Heap_Sort.txt'
SELE = 'Our_Data/Selection__Sort.txt'
BUBB = 'Our_Data/Bubble_Sort.txt'

#variables for comparisions of merge and heap sort. 
#define up here for globals later
c12 = 0
c14 = 0

#simple function for writing to file
#parameters are filename(look at constants above) and the data to write
def write2file(filename, message):
    myfile = open(filename, 'a')
    myfile.write(message + "\n")
    myfile.close()

#funtion to write the different cases to the files
def write2all(message):
    myfile1 = open(MERG, 'a')
    myfile2 = open(HEAP, 'a')
    myfile3 = open(SELE, 'a')
    myfile4 = open(BUBB, 'a')
    myfile1.write("-------------" + message + " CASE------------\n")
    myfile2.write("-------------" + message + " CASE------------\n")
    myfile3.write("-------------" + message + " CASE------------\n")
    myfile4.write("-------------" + message + " CASE------------\n")
    myfile1.close()
    myfile2.close()
    myfile3.close()
    myfile4.close()

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

#python implementation for selection sort
def selection_sort(alist):
   counter = 0
   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(alist)):
           counter += 1
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist, counter


#python implemenation for bubble_sort
def bubble_sort(arr):
    counter = 0
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            counter += 1
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                    
    return arr, counter


# Python implementation of MergeSort

def merge_sort(arr):
    # The last array split
    global c12
    c12 += 1
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):
    global c12
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        c12 += 1
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged



#This Algorithm Was Obtained From GeeksforGeeks.org 
def heapify(arr, n, i): 
    global c14
    largest = i  # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
    
    # See if left child of root exists and is 
    # greater than root
    c14 += 1
    if l < n and arr[i] < arr[l]: 
        largest = l
        
  
    # See if right child of root exists and is 
    # greater than root
    c14 += 1
    if r < n and arr[largest] < arr[r]: 
        largest = r
  
    # Change root, if needed 
    c14 += 1
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
       
  
        # Heapify the root. 
        heapify(arr, n, largest) 
    
# The main function to sort an array of given size 
def heap_sort(arr): 
    n = len(arr)
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 

    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # swap 
        heapify(arr, i, 0)


#Function for testing all the sorts and outputing data to file
def test_suite(arr):
    size_of_array = len(arr)
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    #reseting comparision counter for merge and heap sort.
    global c12
    global c14
    c12, c14 = 0, 0

    #testing bubble sort
    start = timer()
    sorted, counter = bubble_sort(arr1)
    end = timer()
    time = end - start
    write2file(BUBB, "Timing for array size {}: {} seconds.".format(size_of_array, time))
    write2file(BUBB, "Number of comparisions for array size {} is: {}".format(size_of_array, counter))

    #testing selection sort
    start = timer()
    sorted, counter = selection_sort(arr2)
    end = timer()
    time = end - start
    write2file(SELE, "Timing for array size {}: {} seconds.".format(size_of_array, time))
    write2file(SELE, "Number of comparisions for array size {} is: {}".format(size_of_array, counter))

    #testing merge sort
    start = timer()
    merge_sort(arr3)
    end = timer()
    time = end - start
    write2file(MERG, "Timing for array size {}: {} seconds.".format(size_of_array, time))
    write2file(MERG, "Number of comparisions for array size {} is: {}".format(size_of_array, c12))

    #testing heap sort
    start = timer()
    heap_sort(arr4)
    end = timer()
    time = end - start
    write2file(HEAP, "Timing for array size {}: {} seconds.".format(size_of_array, time))
    write2file(HEAP, "Number of comparisions for array size {} is: {}".format(size_of_array, c14))

if __name__ == '__main__':
    
    #creating arrays of different sizes and best and worst case
    print("Generating our lists!")
    size_1000 = rand_array(1000)
    size_10000 = rand_array(10000)
    size_100000 = rand_array(100000)
    best_case = sorted_array_BEST(10000)
    worst_case = sorted_array_WORST(10000)
    
    #average cases
    write2all("AVERAGE")
    print("Starting average case of size 1000!")
    test_suite(size_1000)
    print("Starting average case of size 10000!")
    test_suite(size_10000)
    print("Starting average case of size 100000!")
    test_suite(size_100000)
    
    #best cases
    write2all("BEST")
    print("Starting best case size 10000!")
    test_suite(best_case)

    #worst cases
    write2all("WORST")
    print("Starting worst case size 10000!")
    test_suite(worst_case)
    print("Done with all the sorting! Check the results")
