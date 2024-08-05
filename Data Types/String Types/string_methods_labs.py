"""
Programming Python
Desc: String methods in python
All right reserved lotus studios Oct 2021
"""

"""
# Labs: Test to see if all characters in a predefined string are alphanumeric 
All right reserved lotus code studios Oct 2021
"""
string = "Motiv8"

# testing for alphanumerics
state = string.isalnum()
# print(f"Testing for alphanumerics in {string}\nResults: {state}")


"""
# Labs: Write a function finder that take 2 parameters a character and a string sequence,
 if the character is found print "found" to the console and the index in which its is found.
All right reserved lotus code studios Oct 2021
"""

def finder(char, sequence):
    index = sequence.find(char)
    if index == -1:
        print("Character does not exists in the sequence")
    else:
        print(f"Character {char} found at index {index}")

# print(finder("m", string))


"""
# Labs: Write a function joiner that takes an iterable and a string sequence
the function should return the concatenation of these parameters, use the .join() method.
All right reserved lotus code studios Oct 2021
"""

def joiner(itr, string):
    concat = string.join(itr)
    return concat
db = ['john', 'alice']

# print(joiner(db, " motiv "))


"""
# Labs: Write a function counter() that counts the number of a parameter in another parameter of the function.
All right reserved lotus code studios Oct 2021
"""
def counter(p1, p2):
    _count = 0
    for i in p2:
        if i in p1:
            _count += 1

    return _count

print(counter('n', 'banana'))

"""
# Labs: write a test to open a text file and transverse each word in the file, concatenating 
each word to a single string variables with whitespace as separator, print the concatenated string variable
to the console.
(b) Encapsulate the code written above in a function and find the number of times a particular word occurs
in the concatenated string.
All right reserved lotus code studios Oct 2021
"""

text_file = open("test.txt")
word = list()

for i in text_file.readlines():
    # print(i)
    # splits each word
    word = i.split(" ")

count_d = 0
search = "to"

for i in word:
    if i == search:
        count_d+=1

print(f"The word {search} appears {count_d} times")
print(word)

"""
# Labs: split a string of text in a file.
All right reserved lotus code studios Nov 2021
"""


def str_read(text, numlines):
    lines = text.readlines()
    while lines:
        chunk = text[: numlines]
        lines = text[numlines: ]
        print(chunk,"/n",lines)

print(str_read(text_file, 20))



# text = open("test.txt")

