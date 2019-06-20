# Reference: https://automatetheboringstuff.com/chapter9/
import os

# This has 3 things it returns to loop
# Improved to loop current folder where the program lives in.
for folderName, subfolders, filenames in os.walk(os.getcwd()):
    
    # Outter print statment
    print('The current folder is ' + folderName)

    # Printing all the sub folders
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    # Printing all the filenames
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')
