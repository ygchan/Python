# Reference: https://automatetheboringstuff.com/chapter8/
# A program to write hello world to a text file in Python

# Good monring at 6:07AM!
import os

currentDir = os.getcwd()
f = open('hello.txt', 'w')

f.write('Hello World in Python :)')
# remember to close it
f.close()

print('File is written.')
