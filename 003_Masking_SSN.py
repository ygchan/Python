# Credit: https://automatetheboringstuff.com/chapter7/

# Masking the SSN number using regular expression

import re

# Dummy SSN number to be masking from.

# Prepared a few test cases 
# myString = 'My SSN is 522-00-1234'
# myString = 'Please use my SSN number 022_00_1234'
# myString = 'Yes, number 123121234'

# Testing for multiple SSN :)
myString = 'My SSN: 123-123-1234 and my son SSN: 321-321-4321'

# Using what I learned from the date example
ssnMaskRegex = re.compile(r'''
    \d+      # First group of digit(s)
    \D?      # Optional separator
    \d+      # Second group of digit(s)
    \D?      # Optional separator
    \d+      # Third group of digit(s)
''', re.VERBOSE)

# Use the sub method to return a new string
newString = ssnMaskRegex.sub(r'***-**-****', myString)
print(newString)
