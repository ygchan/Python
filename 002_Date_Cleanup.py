# Credit: https://automatetheboringstuff.com/chapter7/

# Write a program to clean up dates in different from such as
# 3/14/2015, 3/14/2015 and 2015/3/14

# \D match anything except a digit
# ?  match zero or one of the preceding group :)

import re

dateRegex = re.compile(r'''
    (\d+)        # Year or Month
    \D?          # Optional separator
    (\d+)        # Day
    \D?          # Optional separator
    (\d+)        # Year or Month
''', re.VERBOSE)

# myDateString = '3/14/2015'
# They both works!
myDateString = '2015/14/3'

# VERY COMPLICATED DATE...
myDateString = '2015-14-2'

# Testing again
myDateString = '2019_05-06'

mo = dateRegex.search(myDateString)

# There are 3 groups
# mo.group(1) = 3
# mo.group(2) = 14
# mo.group(3) = 2015
print('Group 1 = ' + mo.group(1))
print('Group 2 = ' + mo.group(2))
print('Group 3 = ' + mo.group(3))

groupOne = mo.group(1)
groupTwo = mo.group(2)
groupThree = mo.group(3)

print('\nThe cleaned up date is found as:')

if len(groupOne) == 4:
    # Group 1 is year and yyyy/dd/mm format
    # We wanted to see mm/dd/yyyy
    print(groupThree + '/' + groupTwo + '/' + groupOne)
else:
    # Group 3 is year and mm/dd/yyyy format
    print(groupOne + '/' + groupTwo + '/' + groupThree)
