"""
Programming Python
Desc: Lists in python
All right reserved lotus studios Oct 2021
"""

"""
# Labs: Write a function called nested_sum that takes a list of lists of integers and adds up the
elements from all of the nested lists.
All right reserved lotus code studios Apr 2021
"""

def nested_sum(int_list):
    _sum = 0
    for li in int_list:
        _sum += sum(li)

    return _sum

t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))

"""
# Labs: Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
that is, a new list where the ith element is the sum of the first i+1 elements from the
original list.
All right reserved lotus code studios Apr 2021
"""

def cumsum(_list):
    new_list = []
    count = 0

    for itm in _list:
        x = itm + _list[count]
        new_list.append(x)
        count += 1

        # print(itm)

    return new_list

print(cumsum([1, 2, 3]))

"""
# Labs: Write a function called middle that takes a list and returns a new list that contains all but
# the first and last elements.
All right reserved lotus code studios Nov 2021
"""

def middle(arr):
    new_arr = arr[ 1 : -1]
    return new_arr

print(f"Middle Function: {middle([1, 2, 3, 4,5,6,7,8])}")
