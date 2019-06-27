# https://automatetheboringstuff.com/chapter9/
# Write a python program to add a prefix
import shutil, os, re

# A custom prefix
my_prefix = input('Please enter the new prefix: ')
if len(my_prefix) == 0:
    my_prefix = 'Test'

# To do: Loop over files in the working directory
for python_file in os.listdir('.'):
    # For each file ending with py extension
    if python_file.endswith('.py'):
        # Getting the current working folder absolute path
        absWorkingDir = os.path.abspath('.')

        # new file
        # new_file_name = python_file.replace('Program', 'Testing')
        new_file_name = my_prefix + "_" + python_file
        new_python_file = os.path.join(absWorkingDir, new_file_name)
        
        print(new_python_file)
        # shutil.move(python_file, new_python_file)
