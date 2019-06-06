# Credit: https://automatetheboringstuff.com/chapter7/

# Learning about IGNORECASE, DOTALL and VERBOSE
# You can combine multiple regular expression by using pipe character (|)
# or this is also known as the bitwise or operator

import re

testString = 'some foo bar'

# Using the pipe operator allow you to use multiple operations
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
mo = someRegexValue.search(testString)

if mo != None:
    print(mo.group())
