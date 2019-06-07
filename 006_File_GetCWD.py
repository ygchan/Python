# Reference: https://automatetheboringstuff.com/chapter8/
# A program that ask python where does my program resides in

import os

# OS dot get current work directory
currentDir = str(os.getcwd())
print(currentDir)

# This return a list of string
string_list = currentDir.split(os.path.sep)
# Notice in mac OS X the first element is blank
print(string_list)

# This return a tuple
temp_tuple = os.path.split(currentDir)
print(type(temp_tuple))
print(temp_tuple)

# tuple[0] = directory name
# tuple[1] = base name
print('Directory name: ' + temp_tuple[0])
print('Basename : ' + temp_tuple[1])
