from abc import *

#This is an abstract class
class School(ABC):
    def school_info(self):
        print("Welcome to school")
    @abstractmethod #this declares the abstract method
    def GPA(self):
        pass

#This is a child class
class UCLA(School):
    def GPA(self):
        print("Your GPA is 4.0")

s = UCLA()
s.school_info()
s.GPA()
    
