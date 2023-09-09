
# CPEN 333 Sept 8
# Software Design for Engineers (System Software Engineering before)
# python, OOP
# process management, (multi-processing, multi-threading, synchr, scheduling, os abstraction, real-time systems, concurrency)
# info structures (data structures)
# UML, class library, testing

pass # placeholder (remove and replace with code)


# list (python) vs array (C)
# array - immutable
# list - dynamic (object created based on a class. Methods to expand, change, etc)


# Python - automation, data analysis, machine learning
#        - powerful, modern, high-level, modern general purpose
#        * indentation
# anaconda python 3.11.4 

# Python - interpreted language (not compiled)
#        - checked dynamically (at runtime)

# package manager - conda
# $ conda update all
# $ conda update anaconda
# $ conda update python


# General Structure
print("Hello world") # complete program

# docstring (ignored by Python)
""" multi line
    comment """

# no difference between "" and '' (all string)
print('Hello "Farshid"')
print("Hello \"Farshid\"") # same thing, but need to escape \"


# Variables
# python is dynamically typed
x = 1 # creates variable x
print(type(x)) # <class 'int'>

grade = "A"
print(type(grade)) # <class 'str'>

# no double
# float
percentage = 90.78
print(type(percentage)) # <class 'float'>

# type of variable can change
grade = 1           # int
grade = "hello"     # str

# type hint (not enforceable)
grade: int = 1      # int
grade: int = "hello"  # str


# if elif else
num = 8

if num > 0:
    print("num is pos")
elif num < 0:
    print("num is neg")
else:
    print("num is 0")

# no for loop (need iterator)
for i in range(5):
    print(i) # 0 1 2 3 4 


# fucntions
def func1():
    print("ex 1")

def func2(a, b):
    print(a, "+", b, "=", a+b)

def func3(a,b):
    return a+b

func1()

func2(1.1, 2)

func3(1, 2.1)

# Arithmetic Operators
# **        exponentiation
# //        floor division (like integer division in C)

# Comparison Operators
# == != > < >= <=

# Logical Operators
# and or not

# Bitwise Operators
# & | ~ ^ << >>

# is        true if same object (not equality)
# in        membership - true if x is in y (x is a member of the y object)

# Module
import math
print(math.sqrt(math.sin(math.pi + 1) ** 2))

# Dot Notation
# math.pi        # pi is an attribute of math module


# so this doesn't mess with unit tests
# run this code if this the file you ... run
if __name__ == "__main__":
    pass

# List
list1 = []              # empty list
list2 = [2,3,4]
list2.append(5)         # mutable (now [2, 3, 4, 5])
list4 = [2, "three", 4] # can contain mixed types

