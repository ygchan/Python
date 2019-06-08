# Reference: https://automatetheboringstuff.com/chapter8/
# Writing in plaintext mode and appending in plaintext mode
# Passing a 'w' or 'a' in the second arugment of open()

# If the file does not exist, both argument will create a new file
# But remember to close them before reading the file again.

# About:
# Creating a simple program that ask user for filename (with extension)
# and then create this file and write the message to the file.

import os

filename = input('Please enter the filename: ')
information = input('What do you want to write? ')

currentDir = os.getcwd()
# Create a file with the name defined by user
newFile = open(os.path.join(currentDir, filename), 'w')
newFile.write(information)
newFile.close()

print(filename + ' is created. Thanks!')
