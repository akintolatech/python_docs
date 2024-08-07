"""
Think Python
Desc: Inverse Dictionaries
All rights reserved Lotus Code Studios Dec 2022
"""

def invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        print(val)
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)

    return inverse


sue = {
    "name": "sue li",
    "age": 22,
    "job": "manager",
    "pay": 7000,
}

print(invert(sue))