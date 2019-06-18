# Reference: https://automatetheboringstuff.com/chapter9/
# A program that copy file and folder

import shutil, os

os.chdir('C:\\')

shutil.copy('C:\\spam.txt', 'C:\\delicious')
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')