"""
Python Documentation
Desc: Conditional statements labs
All right reserved Akintola Technologies Apr 2021 updt AUG 24
"""

"""
# Labs: Write a Python if/else statement to assign the smaller of x and y to the variable z. 
given that x = 10, and y = 20.
All right reserved lotus code studios Apr 2021
"""
x = 20
y = 50

if x < y:
    z = x
else:
    z = y

# print(z)

"""
# Labs: Write an if statement that asks for the user's and password via the input() function.
If the password authenticates the predefined password, print to the console "Welcome on board <username>.
Otherwise make it print "check your password". 
All right reserved lotus code studios Apr 2021
"""
# db = {
#     "name": "Motiv8",
#     "password":"123",
# }

name = 'vic'
password = "234"

# input() : collect user data
username = input("Enter Your name: ")
userpass = input("Enter your password: ")

# test for condition
if name != username:
    print("check Username")
if userpass != password:
    print("check password")
else:
    print(f"Auhenticated Successfully\nWelcome on Board {username}")

"""
# Labs: Use the random module to generate a sequence of numbers, then classify the
sequence into 3 classes: low, mid, and high.
All right reserved lotus code studios Apr 2021
"""
import random

sequence = list()

# sequence generator
for i in range(101):
    shell = random.randrange(10)
    sequence.append(shell)

#classifier
classes = [[], [], []]
for i in sequence:
    if i < 3:
        classes[0].append(i)
    elif 3 < i <= 5:
        classes[1].append(i)
    else:
        classes[2].append(i)

# classsifier results
# print(classes)
# sum of items that make up each classes
# print(f"Results------- \nLow: {sum(classes[0])}\nMid: {sum(classes[1])}\nHigh: {sum(classes[2])}\n")

# length of each classes in the classifier
# print(f"Results------- \nLow: {len(classes[0])}\nMid: {len(classes[1])}\nHigh: {len(classes[2])}")


"""
# Labs: Suppose you have two variables x and y defined. Write a stub if statement to evaluate whether x is less than y. 
The statement should not do anything, even if the condition is true.
All right reserved lotus code studios Apr 2021
"""

if x < y:
    pass