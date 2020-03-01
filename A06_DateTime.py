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