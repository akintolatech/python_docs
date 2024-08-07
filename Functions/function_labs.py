"""
Lotus Python Documentation
Desc: Conditional statements
All right reserved lotus code studios Apr 2021
"""

"""
Labs: Write a Python function that checks whether a passed string is palindrome.
All right Reserved Lotus Studios 2021
"""

def palindrome_checker(_str):
    reverse = _str[: : -1]
    if _str == reverse:
        print(f"{_str} is True")
    else:
        print(f"{_str} is False")

    return reverse


print(palindrome_checker("saratu"))







"""
Labs: Write a Python function to check whether a number falls in a given range.
All right Reserved Lotus Studios 2021
"""

def range_check(high, low, n):
    # range computation
    range = high - low

    # conditional checking
    if n <= range:
        print(f"{n} is within the range of {high} and {low}")
    else:
        print(f"{n} is not within the range of {high} and {low}")

print(range_check(40, 7, 90))




"""
Labs: Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
All right Reserved Lotus Studios 2021
"""

def case_counter(_str):
    upper = 0
    lower = 0
    for itm in _str:
        if itm == itm.lower():
            lower+=1
        else:
            upper+=1

    return  f"No. of Uppercase letter: {upper}\nNo. of Lowercase letter: {lower}"

shell = "The quick Brow Fox"

# print(case_counter(shell))






"""
Labs: Write a Python program to reverse a string
All right Reserved Lotus Studios 2021
"""

def str_reverse(_str):
    rev = _str[: : -1]
    return rev

shell = str_reverse("saratu")

# print(f"String Reversal: {shell}")




"""
Labs:define a function manhattan_dist() that take 4 arguements and calculate the manhattan distance of two points in space.
All right Reserved Lotus Studios 2021
"""
def man_dist(x1,x2,y1, y2):
    dist = (x2 - x1)+(y2 - y1)
    return dist

"""
Labs: define a function that take 4 arguements and calculate the manhattan distance of two points in space.
All right Reserved Lotus Studios 2021
"""