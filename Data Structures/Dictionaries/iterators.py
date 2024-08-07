"""
Think Complexity
Desc: Iterator Objects
All rights reserved Lotus Code Studios Jun 2021
"""
d = dict(a=1, b=2)
iter_obj = d.keys()

for key, value in d.items():
    print("{0} => {1}".format(key, value))

for key in d.keys():
    print(key)