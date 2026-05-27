print("*Dictionaries*")

#Dictionary stores data in: key-value pairs.
#Why Dictionarie
#Used for:

#Basic Dictonary
student = {
    "name": "Parth",
    "age": 21,
    "course": "Python"
}
print("Student Dictionary:", student)

#Accessing Values
print("\nAccessing Student Name:", student["name"]+ "\n\n")

#Adding/Updating Values
student["age"] = 22
print("Updated Student Dictionary:", student,"\n\n")

#Loops with Dictionaries
print("Loops with Dictionaries -\n")
for key, value in student.items():
    print(f"{key}: {value}\n\n")
    
# Important Dictionary Methods:
#Method	    Work

#keys()	    all keys
#values()	all values
#items()	both key and value
#get()	    safely get value
#pop()	    remove item

print("List Comprehension with Dictionaries -\n")
# List comprehension is a short and smart way to create lists in Python.
#Instead of writing multiple lines using loops, we can write everything in one clean line.

#Basic Syntax:
#[expression for item in iterable]

lst = []
# res = [i * i for for i in lst]

for i in range(1,6):
    lst.append(i*i)
print(lst)
