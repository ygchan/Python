# Credit: https://automatetheboringstuff.com/chapter7/
# Practice Questions

# Q1. What is the function that creates Regex Objects?
# re.compile
# Example: myNameRegex = re.compile(r'[a-zA-z]+')

# Q2. Why are raw strings often used to create Regex object
# Because you don't have to double escape characters.
# typing \d is much easier than typing \\d

# Q3. What does the search method return?
# It returns a match object.

# Q4. How do you get the actual strings that match the mattern from Match
# object? You use group function/method. If it is not == None, then you
# probably have some match. Try mo.group()

# Q5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group
# 0 cover, group 1 and group 2?
# Group 0 contains the entire strng (matching portion)
# Group 1 contains the area code
# Group 2 contains the phone number

# Q6. Parentheses and periods have specific menaings in the regular expression
# syntax. How would you specify that you want a regex to match actual parenthese
# and period characters?
# You can specify by using escape character in front of them \. and \( and \).

import re
testRegex = re.compile(r'\(\d+\)')
print(testRegex.search('My name is George and (123) to match)').group())

# To be continue tomorrow. :)
