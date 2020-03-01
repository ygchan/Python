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
