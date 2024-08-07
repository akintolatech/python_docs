"""
Programming Python
Desc: Introduction to the list datatype in python programming language
All right reserved Akintola Technologies 27 Nov 23
"""
import random

# list initialisation
strings = list()
num = [1, 2, 3, 6]

# list indexing
print(num[2:])
print(num[:2])

# changing items using index
num[3] = 4
print(num)

# adding items to the end of the list
strings.append("eve")
print(strings)

# list iteration or transversal
names = ["eve", "vic", "su"]

for items in names:
    # do something with each iterated value
    title = "mr"
    # control
    if items == 'eve':
        title = "mrs "
    print(title + items)

more_names = ["jake", "bill"]

# List methods
# list extension extend()
names.extend(more_names)
print(f"extended lists:\n{names}")

# list insertion insert()
more_names.insert(len(more_names), "gates")  # equivalent to more_names.append("gates")
more_names.insert(1, "akin")  # insert item with supplied index insert(i,x)
print(f"After list insertion insert():\n{more_names}")

# list item removal remove()
names.remove('su')
print(f"After list item removal remove():\n{names}")

# list popping pop()
salary = [200, 400, 1000, 10000]
index = 3
salary.pop(index)
print(f"list popped at index {index}\nResulting list is: {salary}")

# clearing list clear()
sal = [200, 400, 1000, 10000]
sal.clear()
print(f"After clearing \n{sal}")

# frequency
scores = [3, 4, 6, 7, 8, 2, 6, 3]
print(scores.count(3))
# Frequency distribution program
distribution = list()
for sample in range(1, 1000):
    seed = random.randint(1, 9)
    distribution.append(seed)

print("Number Generation Complete!")
prompt = int(input("Choose a number from 1 to 9: "))
print(f"Frequency if generation:\t{distribution.count(prompt)}")
print(distribution)

# list sorting sort()

# list reversal reverse()

# list copy copy()

# list stacking

# list as queues
