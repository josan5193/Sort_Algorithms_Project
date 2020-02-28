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

#From geeks for geeks
# Python program for implementation of Bubble Sort
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]), 


# Python program for implementation of MergeSort(geeks for geeks)

# Merges two subarrays of arr[]. 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..r] 
def merge(arr, l, m, r): 
	n1 = m - l + 1
	n2 = r- m 

	# create temp arrays 
	L = [0] * (n1) 
	R = [0] * (n2) 

	# Copy data to temp arrays L[] and R[] 
	for i in range(0 , n1): 
		L[i] = arr[l + i] 

	for j in range(0 , n2): 
		R[j] = arr[m + 1 + j] 

	# Merge the temp arrays back into arr[l..r] 
	i = 0	 # Initial index of first subarray 
	j = 0	 # Initial index of second subarray 
	k = l	 # Initial index of merged subarray 

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			arr[k] = L[i] 
			i += 1
		else: 
			arr[k] = R[j] 
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there 
	# are any 
	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there 
	# are any 
	while j < n2: 
		arr[k] = R[j] 
		j += 1
		k += 1

# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
	if l < r: 

		# Same as (l+r)/2, but avoids overflow for 
		# large l and h 
		m = (l+(r-1))/2

		# Sort first and second halves 
		mergeSort(arr, l, m) 
		mergeSort(arr, m+1, r) 
		merge(arr, l, m, r) 


# Driver code to test above 
arr = [12, 11, 13, 5, 6, 7] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
	print ("%d" %arr[i]), 

mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
	print ("%d" %arr[i]), 

# This code is contributed by Mohit Kumra 


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
