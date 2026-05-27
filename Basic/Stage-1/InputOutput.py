print("*Input/Output Statements*")

def input_output():
    print("This is an example of input and output statements in Python.")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print("Hello",name)
    print("You are",age,"Years old!")


def split_map():
    print("This is an example of using split() and map() functions in Python.")
    print("Using only split() function:")
    Fname = input("Enter your First Name: ").split()
    Lname = input("Enter your Last Name: ").split()
    
    print("Using only map() function:")
    lst = [1, 2, 3, 4, 5]
    op = list(map(str,lst))
    
    
    a,b = map(int,input("Enter two numbers: ").split())
    
    print("Map & Split: ",a + b)
    print("Split: ",Fname ,Lname)
    print("Map: ",op)
    
def Sep_end():
    print("This is an example of using the sep parameter in the print() function.")
    print("Python","Django","RestApi",sep = "-")
    print()
    
    print("This is an example of using the end parameter in the print() function.")
    print("Hello", end = " ")
    print("World!")
    print()
    
    print("Hello", end = " --> ")
    print("World!")
    
def formatted_output():
    name = "Parth"
    Hobby = "Trekking"
    
    print("This is an example of formatted output in Python.")
    print(f"My name is {name} and My Hobby is {Hobby}")
    
    
    

#input_output()
#print()

#split_map()
#print()

#Sep_end()
#print()

formatted_output()
print()




