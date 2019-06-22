# Reference: https://automatetheboringstuff.com/chapter9/
# How to read zipfiles and make zipfiles?

import zipfile, os

# import pretty printer!
import pprint

# Make sure we are in the right folder, the information will report back
# on the terminal.
print(os.getcwd())

# Print out the filename of that zipfile
exampleZip = zipfile.ZipFile('Example.zip')
# print(exampleZip.namelist())

# This look much better! YESSSSSSS :D (DANCE)
pp = pprint.PrettyPrinter()
pp.pprint(exampleZip.namelist())

# Get the file size
quizInfo = exampleZip.getinfo('capitalsquiz3.txt')
print('\n' + str(quizInfo))

print('\nActual filesize: ' + str(quizInfo.file_size))
print('Compressed filesize: ' + str(quizInfo.compress_size))

# Using the %s to 'fillin' the calculated difference
# Original file / Compressed Size = Ratio of how much smaller
# Printing the information using a string formatted.
print('\nCompressed file is %sx smallelr!'
      % (round(quizInfo.file_size / quizInfo.compress_size, 2)))

exampleZip.close()
