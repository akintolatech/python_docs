"""
Functions
Python Documentation
All right reserved Akintola Technologies Updt AUG 24
"""


# A function that adds 2 numbers
def add(num1, num2):
    ops = num1 + num2
    return f"The sum is {ops}"


addition = add(23, 45)
print(addition)

"""
Lotus Python Documentation
Desc: Function statements
All right reserved lotus code studios Apr 2021
"""


# A function that accepts multiple number of arguements
def avg(first, *rest):
    avg = first + sum(*rest) / (1 + len(*rest))
    return avg


# print(avg(1, [2, 3, 4]))

# To accept any number of keyword arguments, use an argument that starts with **. For
# example:
import html


def make_element(name, value, **attrs):
    keyvals = ['%s="%s"' % item for item in attrs.items()]
    attr_str = "".join(keyvals)
    value = html.escape(value)
    element = f"<{name} {attrs}>{value}</{name}>"
    return element


# print(make_element("p", "value"))


# a function that sums up a list
def sum_list(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum


arr = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]

total = sum_list(arr)

print(total)
