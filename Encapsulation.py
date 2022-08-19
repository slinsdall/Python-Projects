


class Encapsulation:
    def __init__(self):
        self.protectedVar = 36 #This is the protected Variable
        self.__privateVar = 14 #Private is done with double __ and is harder to access.

    def getPrivate(self):
        print(self.__privateVar)#This will print the variable we have given it on the screen in shell

obj = Encapsulation() #This defines the obj(object)
obj._protectedVar = 36
obj.getPrivate()
print(obj._protectedVar)
