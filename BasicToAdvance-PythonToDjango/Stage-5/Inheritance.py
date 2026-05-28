print("*Inheritance in Python*\n")

#Inheritance means:

                    #One class can use properties and methods of another class.

#It helps in:

    #code reuse
    #reducing duplicate code
    #making programs organized
    #Real Life Example

#Suppose:

    #Animal → Parent
    #Dog → Child

    #Every dog is an animal.

    #So Dog can use:

    #eat()
    #sleep()

    #without writing again.

    #That is inheritance.
    

#Basic Syntax
    #class Parent:
        # parent properties & methods

    #class Child(Parent):
        # child gets parent features
        
        
#Simple Example
print("Simple Inheritance Example -")
class Animal:

        def eat(self):
            print("Animal eats food")
            
class Dog(Animal):
        pass


d = Dog()
d.eat()

#Output:

    #Animal eats food
    
#What happened?

    #Dog class has no eat() method.

    #But Python searches in parent class Animal.

    #So Dog inherits Animal features.

#Parent Class and Child Class
#Term	Meaning

#Parent Class	Original/Base class
#Child Class	Derived/New class

#Example:

#class Animal:     # Parent
    #pass

#class Dog(Animal):   # Child
    #pass
    
    
#With Constructor Example
print("\nInheritance with Constructor Example -")
class Person:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Student(Person):
    pass


s1 = Student("Parth")

s1.show()

#Output:

#Name: Parth
#How constructor works here

#Student has no constructor.

#So Python automatically uses constructor of Person.


#Adding Child Features
print("\nAdding Child Features -")
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):

    def bark(self):
        print("Barking")

d = Dog()

d.eat()
d.bark()

#Output:

#Eating
#Barking


#Types of Inheritance:

#1. Single Inheritance
print("\nSingle Inheritance -")

#One parent → One child

class A:
    def show(self):
        print("Class A but calling from child class B")

class B(A):
    pass

class_b = B()
class_b.show() 

#Diagram:

#A → B


#2. Multilevel Inheritance
print("\nMultilevel Inheritance -")

#Grandparent → Parent → Child

class A:
    def showA(self):
        print("Class A called from class C")


class B(A):
    def showB(self):
        print("Class B called from class C")


class C(B):
    pass


objc = C()

objc.showA()
objc.showB()

#Diagram:

#A → B → C


#3. Multiple Inheritance

print("\nMultiple Inheritance -")

#One child gets features from multiple parents.

class Father:

    def money(self):
        print("Father's money")


class Mother:

    def care(self):
        print("Mother's care")


class Child(Father, Mother):
    pass


c = Child()

c.money()
c.care()

#Diagram:

#Father
#      \
 #      Child
      #/
#Mother


#4. Hierarchical Inheritance

print("\nHierarchical Inheritance -")

#One parent → multiple children

class Parent:
    def house(self,name):
        print(f"Parent House for {name}")


class Son(Parent):
    pass


class Daughter(Parent):
    pass

s = Son()
d = Daughter()

s.house("Son")
d.house("Daughter")

#Diagram:

 #      Parent
  #     /    \
   # Son   Daughter


#Method Overriding

#Child changes parent method.
print("\nMethod Overriding -")

class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d = Dog()
d.sound()

# Super() Function
#super() is mainly used when:
#Child class has overridden parent method/constructor,but you still want parent version to run too. 

# super() is used when (My personal opinion):
# i want to also run parent class method or constructor having same name as of child class method or constructor.

#Suppose:

#Parent
    #Cook rice
    
#Child overriding
    #Cook biryani
    

#Without super():
    #Only biryani cooked

#With super():
    #First cook rice
    #then add biryani steps
    
print("\nUsing super() -")

class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks): #Here you created a NEW constructor.So Python thinks:“Okay, Student has its own constructor now.
                                     #I will only run Student’s constructor.”So this part never runs automatically now:

                                     #self.name = name
                                     #because it exists inside Person.__init__() so you have to write name as ar
                                     # argument again here.

        super().__init__(name)

        self.marks = marks

    def show(self):
        print(self.name)
        print(self.marks)


s1 = Student("Parth", 90)

s1.show()
