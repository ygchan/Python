# Reference: https://automatetheboringstuff.com/chapter8/

# file object's readlines() method returns a list of string
# from the file, I am guessing it split by \n special character
import os

currentDir = os.getcwd()
filePath = os.path.join(currentDir, 'poem.txt')

# Reading plaintext mode, or read mode for short
# it returns a file object
poemfile = open(filePath, 'r')

# Reading a list of string
string_list = poemfile.readlines()
print(string_list)

poemfile.close()

# Author noted: a list of strings is often easier to work with
# than a single large string value.

# This is very handy when you want to loop them, however, you do
# have to trim the newline character!
