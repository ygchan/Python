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

# Chapter 3: Working with Dates and Time
# how does import statement works?
# how to get today's date? individual components?
# how to get weekday? put it in a list and use it.

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("Today's date is", today)

  # print out the date's individual components
  print("Date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  print("Today's weekday number is:", today.weekday())

  print("Which is: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("The current date and time is ", today)  

  # Get the current time
  # the time function will return only the time part of now
  t = datetime.time(datetime.now())
  print(2)

# How to format date/time?
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%a, %b %y"))

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24 hour time: %H:%M"))

# How to create a time detla?
today = date.today()
print("One year from now: " + str(today + timedelta(days=365)))

april_fool_day = date(today.year, 4, 1)
# Next april fools day
april_fool_day = april_fool_day.replace(year=today.year + 1)

# What is calendar module?
# calendar is a library that allows you to print a string calendar
# or html calendar, it also lets you show what are the days in a month
# weekdays in a month.

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2017, 1, 0, 0)
# print(st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2017, 1)
# print(st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdates(2017, 8):
    print(i)

# The 0 are the dates in that month does not belong to August
for i in c.itermonthdays(2017, 8):
    print(i)

for name in calendar.month_name:
    print(name)

# Show as it with the current local machine
for day in calendar.day_name:
    print(day)

# How to find out the first Friday of every months?
for month in range(1, 13):
	cal = calendar.monthcalendar(2020, m)
	weekone = cal[0]
	weektwo = cal[1]

	# If the first Friday does not belongs to current month
	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		meetday = weektwo[calendar.FRIDAY]

	print("%10s %2d" % (calendar.month_name[m], meetday))

'''
Output:
Team meetings will be on: 
   January  5
  February  2
     March  2
     April  6
       May  4
      June  1
      July  6
    August  3
 September  7
   October  5
  November  2
  December  7
'''

# Q: In Python, what is the correct code format for creating a work 
# calendar with a month that starts on Monday, in June of 2019?

import calendar

cal = calendar.TextCalendar(calendar.Monday)
myCal = cal.formatmonth(2019, 6, 0, 0)
print(myCal)

# Q: When using the timedelta object in Python, how do you use the 
# max, min, and resolution attributes for timedelta?

print(timedelta.max)
print(timedelta.min)
print(timedelta.resolution)   

# Q: Print today's date

from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()
  print ("Today's date is", today)      

# Chapter 04: Reading File
# What is the different between w, r, and a mode?
# How to test what mode your file is reading as?
# How to read and loop a file line by line?
# How to close a file?

def main():
	f = open("textfile.txt", "w+"):
	for i in range(10):
		print("This line is" + str(i) + "\r\n")
	f.close()

	g = open("textfile.txt", "r"):
	if g.mode == "r":
		file_lines = g.readlines()
		for line in file_lines:
			print(line)

	g.close()

if __name__ == "__main__":
	main()

# What is the os module? What is the path module?
# How to get the modification time of a file
# How to get the creation time of a file

# How to check if file exists, a file or directory?

# os gives us ability to work with operate system
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  # Relative path
  print("Item exists: " + str(path.exists("textfile.txt")))
  print("Item is a file: " + str(path.isfile("textfile.txt")))
  print("Item is a directory: " + str(path.isdir("textfile.txt")))
  
  # Work with file paths
  print("Item path: " + str(path.realpath("textfile.txt")))
  print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))
  
  # Get the modification time
  # convert the modification time into a real time
  t = time.ctime(path.getmtime("textfile.txt"))
  # print(t)

  # Another way to get modification time
  # print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  # time delta!
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(
    path.getmtime("textfile.txt")
  )

  print("It has been " + str(td) + " since the file was modified")
  print("or, " + str(td.total_seconds()) + " seconds ")
  
if __name__ == "__main__":
  main()

# Chapter 5: Working with Web Data:
# Getting data from internet - such as JSON, XML, HTML

# What is urllib library? What is a request?
# How to go to a website
# How to check if your connection is sucessful?
# How to get all the html data?

# provide code you need to make http request
import urllib.request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")

  # 200 if ok, 404 errors
  # You are able to connect without errors
  print("result code: " + str(webUrl.getcode()))

  # read the html
  data = webUrl.read()
  print(data)

if __name__ == "__main__":
  main()

# How to parse JSON, XML?
# JSON - use the earthquake as example.

# Q: William is tasked with creating JSON functionality with Python code. 
# What code can he create that reads in JSON data and prints it to the console?

import urllib.request
 def main():
    someUrlData = "http://somerandomJSONdata"
    webUrl = urllib.request.urlopen(someUrlData)
    print("result number: " +str(webUrl.getcode()))
    if (webUrl.getcode() == 100):
       json_data = webUrl.read()
      printResults(json_data)
    else:
       print("No JSON data received, ERROR!") 

# Q: How can you fetch internet data in Python that reads in 200 results 
# from the Bing search engine and prints it out on the display console?
import urllib.request
def main();
  webUrl = urllib.request.urlopen("http://www.bing.com")
  bing_search_results = webUrl.read()
  print(bing_search_results)

# Where next?
# Next video :)
# https://docs.python.org/3/whatsnew/3.8.html


































