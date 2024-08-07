
"""
Think Python
Desc: Dictionaries
All rights reserved Lotus Code Studios Apr 2021
"""

# dictionary initialization
dict1 = dict(name="alice", job="dev", age=40)
dict2 = {"name":"bob",
         "job":"dev",
         "age":40
         }

#iterate over key:value pairs
for i, j in dict2.items():
    print(f"Key: {i}\tValue: {j}")
    pass

#Adding items to a dictionary
dict3 = dict()
dict3["name"] = "sarah"
dict3["job"] = "designer"
dict3["age"] = 25
# print(dict3)

for i, j in dict3.items():
    # print(f"Key: {i}\tValue: {j}")
    pass

#access values only
val = dict3.values()
print(val)

#access keys only
keys = dict3.keys()
print(keys)

# check
itm = "sarah"
print(itm in val)

