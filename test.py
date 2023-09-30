class Count:
    def __init__(self):
        self.count = 0

def increment(c, times):
    c.count += 1
    times += 1

def main():
    myCount = Count()
    times = 0

    for i in range(0, 100):
        increment(myCount, times)

    print("count is", myCount.count, "and times is", times)
    
if __name__=="__main__":
    main()


class Foo:
    def __init__(self):
        self.x = 1
        self.__y = 1

    def getY(self):
        return self.__y

foo = Foo()

msg = "Programming is fun"
print(msg[4: 6])
