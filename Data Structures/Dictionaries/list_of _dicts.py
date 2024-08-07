"""
Think Python
Desc: List of Dictionaries
All rights reserved Lotus Code Studios Jun 2021
"""
bob = {
    "name": "bob smith",
    "age": 42,
    "job": "dev",
    "pay": 3000,
}

sue = {
    "name": "sue li",
    "age": 22,
    "job": "manager",
    "pay": 7000,
}

# lists of dictionaries
db = [bob, sue]

for person in db:
    print(f"{person['name']} collects {person['pay']}")


# print(sue["pay"])
ans = int(input("Enter Sue's Age: "))

if ans == sue["pay"]:
    print("Correct")
else:
    print("Wrong")


# print(db[0])