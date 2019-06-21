# Aautomate the boring stuff with python
# https://automatetheboringstuff.com/chapter9/

# Moving and renaming file/folders.

import shutil

# Making a new copy first
shutil.copy('./hello.txt', './hello_testing.txt')

# Renaing the new copy from hello_testing to bye_bye
shutil.move('./hello_testing.txt', 'bye_bye.txt')

# But let's test if you forgot the file extension and what happen...
# egg is a text file without any extension and create confusion.
shutil.move('./bye_bye.txt', './egg')
