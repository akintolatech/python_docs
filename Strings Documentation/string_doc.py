"""
Programming Python
Desc: Strings Operations in Python
All rights reserved Akintola Technology Feb 2021 updt AUG 24
"""

text = "ivy is a girl"

# string interpolation
print("String Interpolation")
print(f"the string is {text} and the length is {len(text)} and its type is {type(text)}")

# string concatenation
print("String Concatenation")
print("the string is " + text + " and the length is " + str(len(text)) + " and its data type is " + str(type(text)))

# string indexing
text = "victor"

# Slicing operations

slice = text[3:]
print(slice)

print("z" in text)