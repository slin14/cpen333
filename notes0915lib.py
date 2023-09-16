# both "a" and "b" get printed (no problem)
# if this lib.py is imported, only stuff not in if __name__ == "__main__" gets imported


def Foo():
    pass

print("a")

if __name__ == "__main__": # allows this module to be directly run or safely imported
    print("b")
