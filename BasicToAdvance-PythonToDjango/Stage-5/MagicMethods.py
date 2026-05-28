print("*Magic Methods in Python*\n")

#Magic methods are special methods with double underscores.

#Examples:
    #__init__
    #__str__
    #__len__
    #__add__

#All constructors are magic methods BUT Not all magic methods are constructors!

print("__init__() Magic Method - Constructor Example_")

class Student:

    def __init__(self, name):
        self.name = name
        print(f"Constructor Called for {self.name}\n")
        
s1 = Student("Parth")
#--------------------------------------------------------------
print("__str__() Magic Method Example_")

#__str__() Controls object printing.

class Student:

    def __str__(self):
        return "Student Object"


s1 = Student()

print(s1)