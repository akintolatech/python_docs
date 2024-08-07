"""
Programming Python
Desc: Strings methods in Python
All rights reserved Lotus Studios Dec 2022
"""

text = "xxx Spam xxx"

# finding text:returns the index where the first letter is found
pos = text.find("Spam")

# index was used to slice the text
# print(text[pos:])

# replacing chunks of text
rep = text.replace("Spam", "Ram")
# print(rep)


# the in membership operator can also be used to find substrings of text
if "Spamx" in text:
    # print(True)
    pass
else:
    # print("Not found")
    pass

# splitting strings using a specified delimiter (,): Default liimiter is whitespace
_string = "akintola, victor, ayo"
splitted = _string.split(",")
# print(splitted)


# joining
new_text = ["as surname is ", "as first name ", " as last name"]
joined = _string.join(new_text)
# print(joined)

# converting lists to strings
# list instantiation
chars = list("loretta")
# print(chars)

# conversion: joining the list with empty delimiters
print("".join(chars))
