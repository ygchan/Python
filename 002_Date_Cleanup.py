# Credit: https://automatetheboringstuff.com/chapter7/

# Write a program to clean up dates in different from such as
# 3/14/2015, 3/14/2015 and 2015/3/14

import re

dateRegex = re.compile(r'''
    (\d+)        # Year or Month
    /            # Optional separator
    (\d+)        # Day
    /            # Optional separator
    (\d+)        # Year or Month
''', re.VERBOSE)

# myDateString = '3/14/2015'
# They both works!
myDateString = '2015/14/3'
mo = dateRegex.search(myDateString)

# There are 3 groups
# mo.group(1) = 3
# mo.group(2) = 14
# mo.group(3) = 2015
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))

groupOne = mo.group(1)
groupTwo = mo.group(2)
groupThree = mo.group(3)

if len(groupOne) == 4:
    # Group 1 is year and yyyy/dd/mm format
    # We wanted to see mm/dd/yyyy
    print(groupThree + '/' + groupTwo + '/' + groupOne)
else:
    # Group 3 is year and mm/dd/yyyy format
    print(groupOne + '/' + groupTwo + '/' + groupThree)
