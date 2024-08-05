"""
Programming Python
Desc: String methods in python
All right reserved lotus studios Oct 2021
"""

string = "Motiv8 Technologies"

# string methods
# length of string
string_len = len(string)
# print(string_len)

# capitalize
caps = string.capitalize()

# uppercase
upper = string.upper()

# lowercase
lower = string.lower()

# count
string_count = lower.count('o')
# print(string_count)


# find method
sub = "tiv"
# string index
sub_index = string.find(sub)
# print(f"Substring found at: {string[sub_index]}")

# testing for alphabeths
state = string.isalpha()
# print(f"Testing for alphabet in {string}\nResults: {state}")

# swapcase
swapped = string.swapcase()
# print(swapped)

# # title
title = string.title()
# print(title)



