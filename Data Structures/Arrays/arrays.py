"""
Data Structures
Desc: Working with array module
All rights reserved Lotus Code Studios May 2021
"""
from array import *
# initialising arrays with type code
my_array = array('i', [1,3,4,5])

#appending elements to an array
my_array.append(6)

#insert an element to an array: slow operation
my_array.insert(3, 1)

#extend an array into a new array
my_array2 = array('i', [6,8,3,7])
my_array.extend(my_array2)
print(f"After Extension: {my_array}")

#remove elements from an array (time inefficient): remove()
my_array.remove(7)
print(f"Remove element 7: {my_array}")

#remove the last element from an array (time efficient): pop()
my_array.pop()
print(f"Pop last element: {my_array}")

#reverse array: reverse()
my_array.reverse()
print(f"Reversed array: {my_array}")

#get buffer info from array
print(f"Buffer info: {my_array.buffer_info()}")

#count the occurence of an element in an array: count()
print(f"Count : {my_array.count(6)}")



