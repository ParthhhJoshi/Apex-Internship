print("*Encapsulation in Python*\n")

#Encapsulation means keeping data and the functions that use that data together inside a class, 
#and protecting important data from direct misuse.

#Encapsulation = keeping related data and functions together safely inside a class.

# Encapsulation helps organization and protection That’s it.

#Simplest Example

class Student:

    def __init__(self):
        self.name = "Parth"

    def show(self):
        print(self.name)
s1 = Student()
s1.show()
        
#Here:
    #name = data
    #show() = function using that data

    #Both are inside one class.This itself is encapsulation.
    
#Main Idea You Need
    #Instead of doing:

        #name = "Parth"

            #def show():
                #print(name)

#OOP keeps everything organized inside class:
    #class Student:
            #This is why Django heavily uses classes.
            
            