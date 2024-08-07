"""
Programming Python
Desc: Membership operators and operations
All right reserved Motiv8 Technologies Mar 2021
"""

# get input strings
_str = input("Enter your String: ")

#text to query
text = "motiv8 Technologies"

# the state of membership
state = _str in text.casefold()
print(state)

# condition to check
if state:
    print(f"the string {_str} is in {text}")
else:
    print(f"the string {_str} is not in {text}")


