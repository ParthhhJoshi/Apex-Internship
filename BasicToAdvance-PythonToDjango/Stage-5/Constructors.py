print("*Constructors in Python*\n")

#__init__() LOOKS like a normal function, but Python gives it a special meaning.

#That special meaning makes it a constructor.
 #Normal Function

#Example:

#class Student:

    #def show(self):
        #print("Hello")
#s1 = Student()
#s1.show()


#Constructor

#class Student:

    #def __init__(self):
        #print("Constructor Called")
#-------------------------------------------------------------------------------------------------------------------

def constructor_without_parameters(): #Default Constructor
    class Student:

        def __init__(self):
            print("Constructor without Parameters Called")

    s1 = Student()


def constructor_with_parameters():
    class Student:

        def __init__(self, name, age):# No need to call this function, it will be called automatically when we create an object.
            self.name = name
            self.age = age

        def show_data(self):
            print("Constructor with Parameters Called")
            print("Name:", self.name)
            print("Age:", self.age)

    s1 = Student("Parth", 20)

    s1.show_data()
    
def constructor_with_default_values():
    class Student:
        def __init__(self, name = "unknown"):
            self.name = name

        def show_data(self):
            print("Constructor with Default Values Called")
            print("Name:", self.name)
    s1 = Student()
    s2 = Student("Parth")
    
    s1.show_data()
    print()
    s2.show_data()

    
    
constructor_without_parameters()
print()

constructor_with_parameters()
print()

constructor_with_default_values()
print()


