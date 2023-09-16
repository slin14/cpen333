# Sept 15 - OOP
import tkinter # import entire module ("library") (not messing with namespace)
root = tkinter.tk()

from tkinter import tk # only import tk from module
                       # binding the namespace (not used as often)
root = Tk()


# if "__name__" of this current module is "__main__", run these ...
# __ "dunder" (double underscore)
# allows the module (*.py) to be directly run or safely imported
# if module is imported, stuff below will not be run
if __name__ == "__main__:
    #...
