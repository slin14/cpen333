# Sept 15 OOP

class ClassName:
    pass
    #initializer
    #methods


print ("hello world") # python allows procedural

# bare minimum of a class
class Foo:
    pass

class Foo2:
    # initializer (method)
    # run automatically when you create an object of this class
    def __init__(self): # "self" is python convention (could be any str)
                        #        references the object itself
                        #        used in instance methods
                        #        acess data fields in class
                        #        used when involking methods in methods
        self.x = 1      # datafield


# use class
f = Foo2() # instantiate (creates object & assigns datafield)

print(Foo2, f, f.x)
#         <class '__main__.Foo2'> <__main__.Foo2 object at 0x00000154CC64B3A0> 1
#                   class
#                   object
#                   datavalue == 1

#####################################################################
# class - create a type
#         eg. BMI

class BMI:
    """ """

    # datafield - data values that are important for this type
    #             not intermediate values

    # initializer
    def __init__(self, name, weight, height): # self is not a parameter when using the initializer
        self.__name = name # self.<> makes it a datafield
                           # "name" itself is the parameter

    def getBMI(self) -> float:
        pass

    def getStatus(self) -> str:
        pass


# using the class


#####################################################################
import math
class Circle:
    def __init__(self, radius = 1): # initializer
        self.radius = radius        # data field

    def getPerimeter(self):
        return self.radius * math.pi * 2

    def getArea(self):
        return self.radius * self.radius * math.pi


# using the class Circle
circle0 = Circle(5) # just need radius
circle1 = Circle()  # default radius = 1

print(circle0.getPerimeter()) # object.method()


#####################################################################
class Dog:
    kind = 'canine' # class variable shared by all instances !!!


#####################################################################
# data hiding (for good citizens)
class Foo:
    def __init__(self, bar = 1):
        self._bar = bar   # single underscore indicate private field
                          # not enforceable !

    def __init__(self, bar = 1):
        self.__bar = bar  # double underscore enforced by name mangling
                          # to provide name hiding (better !)

#####################################################################
# str class
s1 = ""      # s1 = str()
s2 = "hello" # s2 = str("hello")

# immutable, so new object is created
s2 = "hello again" # id() is changed

# many methods ...

#####################################################################
# exception handling

# happens at runtime -> program crashes
# must be handled at runtime

try:
    print(1/0)
except:
    print("bad things happened") # now program doesn't crash
    # try to do damage control, then stop the program

try:
    # as small as possible (only code to guard exception against) 
except ZeroDivisionError:
    pass
else:
    # handler for no exception occurred (optional)
finally:
    # executed always
    # for cleanup (resources: eg. close files)

#####################################################################
