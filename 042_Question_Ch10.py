# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# Practice Questions
# 01. Write an assert statement that triggers an AssertionError
# if the variable spam is an integer less than 10.

spam = 100
# Remember, if you want it to throw error if it is less than 10
# then you have to test if it is greater than 10.
# Less than 10 is the error condition, not the expression for assert.
assert spam >= 10, 'Your spam is less than 10!'

# 02. Write an assert statement that triggers an AssertError if
# the variable eggs and bacon contain strings that are the same as each other
# even if their cases are different.
eggs = 'hello'
bacon = 'good bye'

# Raise an AssertError if they are not different.
assert eggs.lower() != bacon.lower(), 'eggs/bacon should not be the same!'

# 03. Write an assert statement that always triggers an AssertionError.
# assert True, 'Always triggers an AssertionError.'

# 04/05. What are the two lines that your program must have in order to have
# logging.debug() send a logging message to a file named programLog.txt?
import logging
logging.basicConfig(
    filename='programLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Test a logging.debug('message')
#  2019-08-03 12:24:50,549 - DEBUG - This is a test message.
# logging.debug('This is a test message.')

# 06. What are the 5 logging levels.
# logging.debug() - variable's state and small details
# logging.info() - general events, confirm a program is working
# logging.warning() - potiental problem to work on in the future
# logging.error() - record an error that caused program to fail to do something
# logging.critical() - fatal error that has caused

# 07. What line of code to add to disable all logging messages
logging.disable(logging.DEBUG)

# 08. Why is using logging messages better than using print() to display
# the same message?
# Because with print, when your program is ready for production, you still
# have to "remove" or comment it out. Verses logging message, you can toggle
# the setting on/off or write to a file (send to a server). It is more flexible
# especially with logging level 1-5.

# 09. What are ther difference between Step, Over and Out buttons in the
# Debug Control Window?
# Step - one line execution at a time
# Over - excecute the next line of code, but if it is a program, it will
#        complete the entire function call.
# out  - execute the lines of code unti it returns from the current function.
#        (out is useful when you stepped into a function call).

# 10. After you click Go in the Debugger, when will it stop?
# Go runs until the program terminate or reaches a breakpoint set.

# 11/12. What is a breakpoint? How to create it?
# When you have Debugger enabled and you can right click on any lines
# to create a breakpoint. During Go - it will stop there and await your next
# command.
