#!/usr/bin/python3
import random

MERG = 'Merge_Sort.txt'
HEAP = 'Heap_Sort.txt'
SELE = 'Selection_Sort.txt'
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
