"""
Programming Python
Desc: String operations in python
All right reserved Motiv8 Technologies Mar 2021 updt Aug 24
"""

# strings are sequence of characters
_str = "Hello lotus"


print(_str.count('e', 0 , 5))

sign = "$"
amount = "5000"

# string concatenation
print(sign + amount)

# string membership
print(sign in amount)
print(sign not in amount)

#string indexing
story = "Minna is in Nigeria"
# print(story[-1])

# string slicing
minna = story[0:5]

# omitting the last index
all = story[0: ]

# omiting the first index
minna2 = story[ : 5]

# strides
stride_test = story[2 : 4 : 6]

# print(stride_test)

# string interpolation
name = "lotus"
balance = 5000

# interpolation
print(f"Your name is {name} and your balance is {balance}")

print("Interpolated: Your name is:", name, "and your balance is: ", balance)

# string concatenation
print("Your name is:" + name + "and your balance is: " + str(balance))

# using the format method
print("Your name is {0} and your balance is {1}".format(name, balance))





