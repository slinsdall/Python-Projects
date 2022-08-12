
#Parent Class
class User:
    name = 'Sarah'
    email = 'sk@gmail.com'
    password = 'PassWord!'

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")
            
#Child class
class Teacher(User):
    ID = 115
    Class = 'Computer Science'

    #Same method as parent class, only difference is asks for id rather than name
    def getLoginInfo(self):
        entry_Id = input("Enter your ID: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_Id))
        else:
            print("The password or email is incorrect.")

            
#another child class instance
class Student(User):
    Major = 'Computer Science '
    Grade = 'B+'
    pin = '2589'

    #Uses same method as parent only with a pin instead of password
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")

if __name__ == "__main__":
    teacher = Teacher()
    print(teacher.getLoginInfo())
 
    student = Student()
    print(student.getLoginInfo())
    
            
