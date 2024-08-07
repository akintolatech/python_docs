"""
Programming Python
Desc: List Operations
All right reserved Akintola Technologies 27 Nov 23
"""

# check if an item is in the list
staffs = ["eve", "vic", "su"]
new_staff = "ana"

print(new_staff in staffs)

if new_staff not in staffs:
    print("You are not a staff!")

# list traversal
for staff in staffs:    #read only
    print(staff)

salary = [200,500,400]
# for i in range(len(staffs)):
#     staff[i] =