


class Encapsulation:
    def __init__(self):
        self.protectedVar = 36

obj = Encapsulation()
obj._protectedVar = 36
print(obj._protectedVar)

class Encapsulation:
    def __init__(self):
        self.__privateVar = 14

    def getPrivate(self):
        print(self.__privateVar)


obj = Encapsulation()
obj.getPrivate()

