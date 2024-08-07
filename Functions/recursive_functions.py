"""
Lotus Python Documentation
Desc: Recursive Functions
All right reserved lotus code studios Apr 2021
"""

def countdown(n):
    if n <= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n-1)

print(countdown(10))

# write a function that prints a string n times
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    # print_n(s, n-1)



