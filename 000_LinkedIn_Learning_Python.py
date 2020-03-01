# Chatper 01: Setup
# Download sample files
# Check version using this command.
# python 3 --version

# Run certificate command for web access later on
# Download Visual Studio from https://code.visualstudio.com/

# Install and setup launch.json

# Q: Why is Visual Code good for creating Python projects? 
# A: Visual Code is an IDE that creates Python projects fast and easy. 

# Q: How can you check which version of Python is on a MAC operating system?
# A: Python -v

# Chapter 02: Python Basic
# How to start python on terminal?
# python 3 or python

# Python is an interpted language, the program does not need to be compiled
# in order to execute it. 

2 + 2
print("Hello World")

exit() # Calling the exit function, place the ()

# To run your program in terminal, cd to folder and do python3 <python program name>
# Put your program in main and then calls it

# Comment are define by # symbol.
# Python is strongly type lanugage, even you don't need to define it,
# it still infer the type, so you can't combine with different types.
# Unlike javascript, when it see you do print("string" + 123), it will print.

# How to convert a number to string
str(123) # now "123"

# Global vs. local variables
# Even if they are they are the same name, they are interpted differently.

# # re-declaring the variable works
f = "abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("this is a string" + str(123))

# Global vs. local variables in functions
def someFunction():
    f = "def"
    print(f)

someFunction()
print(f)

# How to define a function?
def func1():
	print("I am a function")

# what is the scope definer in python? colon (:)

func1() # Normal way to call and get printed
print(func1()) # The outter print NONE
print(func1) # Printing the function definition, the function is not be executed.
# function definition is evualted to a <... string .... >

'''
I am a function
I am a function
None
<function func1 at 0x105827488>
'''

# how to define multi argument, default argument?
def func2(num=1):
	print(num)

def func3(*arug):
	result = 0
	for num in arug:
		result = result + num
	return result

# If you want to affect it inside the fucntion.
def someFunction():
	global f
	f = "def"
	print(f)

someFunction()
print(f)

# condition if / elif / else statement
# python does not have switch case

# Review
# conditional statements let you use "a if C else b"
st = "x is less than y" if (x < y) else "x is greater than or the same as y"

# What are the two different loops python has? while/for

# define a while loop
# while loop execute while the condition is True
while (x < 5):
	print(x)
	x = x + 1

# define a for loop
# There is no index counter variable
# Python loops are iterators, use the range to return the range of numbers 
# 10 is not inclusive in the range, this prints out 5-9
for x in range(5, 10):
	print(x)

# How to define a class?
# What is self? Self is reference to current object itself. Similiar to This 
# in javascript.

# How to inherent a class? (Super Class)?
class myClass():
  # the self argument refer to the object itself, like this in javascript
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

class anotherClass(myClass):
  # the self argument refer to the object itself, like this in javascript
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2")

def main():
  # create instance of myClass object
  c = myClass()
  # then you can start calling the functions
  c.method1()
  c.method2("This is a string")

  c2 = anotherClass()
  # invoking myClass method 1 and then anotherClass method 1 print message
  c2.method1() # inherenced method of super class

  c2.method2("Another String") # overwrite the myClass method 2

# How to overwrite the class function?

# Q: In Python, what is the correct way to develop a class called Person 
# that has parameters in the initialize function called name, age, and sex?

class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex 

# Q: Juan has a task of adding loops to his Python project. 
# How can he create if loops that check greater than values?

if 10 > 20:                           
	print('This conditional statement is false')         

if 10 < 20:                        
    print('This conditional statement is true')  

# Q: Sunita is adding conditional structures in Python. 
# What is the correct way to create an if conditional structure that 
# loops 50 times and displays the food called "roast"?

food = 'roast'

if food == 'roast':
    print('Ummmm, my favorite!')
    print('I feel like saying it 50 times...')
    print(50 * (food + '! '))

# Q: Robert is creating a basic function in Python. 
# How should he create a function that displays "This is a basic Python function!"?

def funcBasic(): 
   print("This is a basic Python function!")

# Q: Johanna is learning the evaluation order of Python expressions and operators. 
# What evaluation order should she follow when creating an expression in Python 
# that has the results of 14?

length = 5
breadth = 2
print('Perimeter is', 2 * (length + breadth))

