"""
Programming Python
Desc: Simple intrest in python
All right reserved Motiv8 Technologies Mar 2021
"""

"""
# Labs: Write a function simple_intrest() that takes 3 parameters p, r, t and use it
to compute the simple intrest formula
All right reserved lotus code studios Oct 2021
"""


def simple_intrest(p, r, t):
    intrest = p * r * t / 100
    return f"The intrest for the Principal of {p} at the rate of {r} for the duration of {t} years is {intrest}"


print(simple_intrest(40, 5, 5))
