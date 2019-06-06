# Credit: https://automatetheboringstuff.com/chapter7/

# Using bitwise operator to write a regular expression that
# ignore case and allow you to match everything including a new line

import re

myString = 'This is a newline,\nFollow by another line'
newLineRegex = re.compile(r'.*', re.DOTALL | re.I)

mo = newLineRegex.search(myString)
print(mo.group())
