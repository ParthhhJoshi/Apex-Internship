print("*Polymorphism in Python*")

#Poly = many
#Morphism = forms

#Same function behaving differently.

class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()
