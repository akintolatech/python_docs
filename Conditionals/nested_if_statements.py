"""
Lotus Python Documentation
Desc: Nested conditional statements
All right reserved lotus code studios Apr 2021
"""

x = 0
y = 1

# nested conditionals
if x > y:
    print("greater")
    if x == 100:
        print("X is 100")


if x > y and x == 100:
    print("merged Successfully")


# ternary operators
var = "greater" if x > y else "Lesser"
print(var)