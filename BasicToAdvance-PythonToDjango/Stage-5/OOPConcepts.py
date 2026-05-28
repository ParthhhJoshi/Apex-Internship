print("*OOP Concepts: *")

#1. Classes & Objects
    #Real Life Example

#Think about:

#Class = Blueprint
#Object = Real thing made from blueprint

#Example:

#Car = class
#BMW, Audi = objects

#Syntax
#class Student:
    #pass

#Creating object:

#s1 = Student()

print("Example of Class and Object -\n")
class car:
    def show(self):
        print("This is a car.")
    
c1 = car()
c1.show()
#Real-Life Analogy

#Imagine:

    #Class = House Blueprint
    #Object = Actual House
    #self = Particular House (You can use any name instead of self, but self is a catching variable name)

#Storing Data in Objects

class student:
    def setdata(self,name,age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Student Age: {self.age}")

s1 = student()
name = input("Enter student name: ")
age = int(input("Enter student age: "))
s1.setdata(name, age)
s1.show_data()

#Object = Data Container

#Think of object like a box.

    #s1 → box containing Parth
    #s2 → box containing Rahul

#self tells Python:
    #Use the data from THIS box

#Most Important OOP Concept
    #Class creates structure
    #Object stores actual data
    #self connects methods to that object's data
    
#In Python class methods, self (or whatever name you choose) must be the first parameter.