"""
Think Python
Desc: Histogram Implementation
All rights reserved Lotus Code Studios Apr 2021
"""
def histogram(data):
    _dict = dict()
    for itm in data:
        if itm not in _dict:
            _dict[itm] = 1
        else:
            _dict[itm] += 1
    return _dict

def loop(data):
    # sorts the dataset
    for i in sorted(data):
        print(f"{i} => {data[i]}")
    return " "


data = "fanta"
hist = histogram(data)

sorted = loop(hist)





