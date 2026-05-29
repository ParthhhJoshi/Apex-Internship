import List


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
# res = [i * i for i in lst]

for i in range(1,6):
    lst.append(i*i)
print(lst,"\n")

#Most Important Examples:

print("Square of numbers using List Comprehension:")
res = [i * i for i in range(1  ,6)] 
print("Result: ",res) 

print("\nEven numbers using List Comprehension: ")
n = int(input("Enter the range for even numbers: "))
even_num = [i for i in range(1,n + 1) if i % 2 == 0]
print("Even Numbers: ",even_num)

print("\nOdd numbers using List Comprehension: ")
n = int(input("Enter the range for odd numbers: "))
odd_num = [i for i in range (1 , n + 1) if i % 2 != 0]
print("Odd Numbers: ",odd_num)

print("\nConvert to Uppercase using List Comprehension: ")
uppr_lst = ['hello', 'world', 'python', 'programming']
uppr = [uppr_name.upper() for uppr_name in uppr_lst]
print("Uppercase List: ",uppr)

print("\nIf-Else in List Comprehension: ")
nums = [1, 2, 3, 4, 5]
res = ["Even" if i % 2 == 0 else "Odd" for i in nums]
print(nums)
print("Even or Odd: ",res)


#Important Rules
#Rule 1 — Expression Comes First    
                                #[i * 2 for i in range(5)]

#NOT:

                                #[for i in range(5) i * 2]
                                
#Rule 2 — if Comes After Loop
                                #[i for i in nums if i > 2]
                                
#Rule 3 — Works with Strings, Lists, Tuples, Range
                                #[ch.upper() for ch in "python"]
                                

                        #One-Line Summary

#List comprehension = Create a new list using loops and conditions in one short line.
