# Credit: https://automatetheboringstuff.com/chapter8/
# Practice Questions on the back of the chapter

# Question 01: What is a relative path relative to?
# Relative path is related to the directory where the folder resides in.

# Question 02: What does an absolute path start with?
# An absolute path on differet operating system:
# Window: C:\ ... (Backward Slash)
# Unix and Mac OS: /.... (Foward Slash)
# Refresher: P.174 - Backslash on Window and Forward Slash on OS X
# If you want the program to works on both system, use os.path.join()
# The python module will handle picking for you :)

# Question 03 (**) : What do the os.getcwd() and os.chdir() functions do?
# os.getcwd() = Get current work directory, it returns the absolute path of
# where the python script resides in in a string form.
# os.chdir() = This will change where current work directory is pointing to.
# (kind of like changing folder path). Because any filename or paths that do
# not begin with a root folder are assumed to be working under the current
# working directory.

# On the other hand, if you are given a full path (with file).
# You can then call os.path.basename() and os.path.dirname()
# respectively to get the filename with extension and folder

# Question 04 (***) : What are the . and .. folders?
# (. and ..) are not real folders - they are special names that can be used
# in a directory. single dot = this current directory, and two periods (dot dot)
# = the parent folder.

# Question 05: In C:\bacon\eggs\spam.txt, which part is dirname, basename?
# dirname = C:\bacon\eggs << no backslash here!
# basename = spam.txt     << with extension here!

# Interestingly - when george was trying to compile this.
# myString = r'/User/bacon/eggs/spam.txt'
# Because it is the Mac OS system :)

# Question 06: What are the 3 modes that can be passed to open() function?
# a = append - create file if not exists
# w = write  - create file if not exists
# r = ready only

# Question 07: What happen if an existing file is opened with "w" mode?
# It will overwrite the file.

# Question 08 (***): What is the difference between read() and
# readlines() function?
# read() = read everything into memory as string.
# readlines() = return a list of string values from the file. << Userful :)

# Question 09 (***): What data structures does a shelf value resemble?
# Dictionary, you can access these "setting" by doing this

# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Bobo']
# shelfFile['cats'] = cats << Storing the cats list into shelfFile
# shelfFile.close()

# I think the citibike project can use this too. 
