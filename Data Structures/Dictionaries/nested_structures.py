"""
Programming Python
Desc: Nested Structures
All rights reserved Lotus Code Studios Jun 2021
"""

# nested structures examples
bob = {
    "name": {"fname":"bob", "lname":"smith"},
    "age": 42,
    "job": ["fullstack", "content management"],
    "pay": (7000, 3000),
}

# print all of bobs jobs
for item in bob['job']:
    print(item)
    # pass

print(bob["name"]["lname"])