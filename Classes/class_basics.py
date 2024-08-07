"""
Python for dummies
Desc: Class Basics
All rights reserved Lotus Code Studios Apr 2022
"""

class My_class():

    # class variable
    my_var = 10

    #instance methods
    def say_hello(self):
        # print("Hello")
        # instance variable
        text = "hello"
        return text

class Greet():
    # class constructor
    def __init__(self, name="vic"):
        self.Greeting = name+" !"

    def call_greeting(self):
        return f"Hello {self.Greeting}"

# class instantiation
my_inst = My_class()
#acessing class variables
# print(my_inst.my_var)

# print class attributes
# print(dir(my_inst))
# print(my_inst.say_hello())


hailing = Greet("Abimbola")
print(hailing.call_greeting())


