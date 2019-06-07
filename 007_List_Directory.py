# Reference: https://automatetheboringstuff.com/chapter8/
# A program that list the filename in the current directory

import os

# Print the list of filename in our directory
currentDir = os.getcwd()
filename_list = os.listdir(currentDir)

# Sorting it to look pretty.
filename_list.sort()

# Print out what the list contain
print(filename_list)
print(str(type(filename_list)) + '\n') # A list!

# Print the header
print('Filename'.ljust(50) + '|' + 'FileSize'.rjust(10))

# Loop each file and print it out
for filename in filename_list:
    # If the file is a python source file
    if filename.endswith('.py'):
        # Use path.join to apply proper forward slashes
        myString = os.path.join(currentDir, filename)
        mySize = os.path.getsize(myString)
        # Display it to the user
        print(myString.ljust(50) + '|' + str(mySize).rjust(10))
