"""
Programming Python
Desc: Boolean operators and operations
All right reserved Motiv8 Technologies Mar 2021
"""
import random

# Create a function draw that takes two arguements name and bet, set a random state and multiply the value
#by the supplied bet, if the result is greater than or equal to 15 print a success note else print try again
# good luck !!!
def draw(name, bet):
    state = random.randrange(1, 10)
    shell = bet * state
    if shell >= 15:
        print(f"Congrats {name} you got {shell}")
    else:
        print(f"Try again")
    return 0

print(draw("vic", 4))