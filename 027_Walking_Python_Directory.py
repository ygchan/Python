# Reference: https://automatetheboringstuff.com/chapter9/
# Best book ever!

import os

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    # print('Folder: ' + folderName)
    # I think this is cleaner, less information :)
    print(folderName)

    for subfolder in subfolders:
        # print('\tSubfolder: ' + subfolder)
        print('\t' + subfolder)

    for filename in filenames:
        print('\t' + filename)

    # The filenames are list type, but can't be easily sorted because there
    # are NoneType in there.
    print(type(filenames))
