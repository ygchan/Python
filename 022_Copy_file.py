# Aautomate the boring stuff with python
# https://automatetheboringstuff.com/chapter9/

# In chapter 8 I learned how to create, append and write to new files w/ Python.
# Also to get directory, change current work directory, create file paths.

# This chapter will teach me the tools to organize file,
# such as copying, renaming, moving or compressing them.

# Think of targeting in particular file type, or filename setup.
# Or modifying the way files are named.

# Quote from the author: "All this boring stuff is just begging to be
# automated in Python. Create a program to do them quickly and not make mistake!

# First step is the Shutil (Shell Utilities) Module.
# Shutil provides functions to copy, move, rename and delete files.

# Shell Utilities module
import shutil, os

# Print the current directory
current_dir = os.getcwd()
print(current_dir)

print('The files are now copied and renamed!')
shutil.copy('/Users/Study/Python/hello.txt', '/Users/Study/Python/bye.txt')

# Remember in window it must be escaped... C:\\ instead of C:\
# And as a bonus if you don't supply the full path, it works too!
# Assume the file is in the current work directory.

shutil.copy('hello.txt', 'bye2.txt')

# Backup the whole bacon folder :)
shutil.copytree('./bacon', './bacon_backup')
