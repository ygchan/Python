# Reference: https://automatetheboringstuff.com/chapter8/

# Learn how to use Python to create, read and save files on the hard drive.
# There are 2 parts of a file
# 1. filename, with file extension separated by a dot
# 2. path of folder, or directories

# Window Style folder C:\
# Mac and Linux style folder /
# Note: File and folder are not case sensitive on Window and OS X
# But they are on Linux environment.

# Backslash \ on Window
# Forward Slash / on OS X and Linux
# If you want your program to works on both, you need to account of this.
# But Python has a library that handles it for you :)

import os

print(os.path.join('user', 'bin', 'spam'))
