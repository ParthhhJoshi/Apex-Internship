print("*Abstraction in Python*\n")

#Abstraction is the idea of hiding complex details and showing only the essential features of something.


#Difference Between Abstraction & Encapsulation
#Concept	    Meaning
#----------------------
#Abstraction	Hiding complexity
#Encapsulation	Protecting data

#Simple Class Example
class Car:

    def start(self):
        print("Car Started")

c1 = Car()
c1.start()

#User only does:
    #c1.start()

#User doesn't care:
    #fuel injection
    #engine process
    #battery system
    
#All hidden.That is abstraction.
