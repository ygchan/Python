# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# Assertion is a sanity check to make sure your code isn't doing something
# obviously wrong. You may do so using the assert statement.
#   - assert keyword
#   - a condition (expression that evaluates to True or False)
#   - a comma
#   - a string to display the False condition

my_door_status = 'open'
assert my_door_status.lower() == 'open', 'The door needs to be "open".'

# This is a really scary reference. Good movie tho.
my_door_status = 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
assert my_door_status.lower() == 'open', 'The door needs to be "open".'

# An assert statement:
# I assert this condition to be true, if not, there is a problem (bug) in
# your program. If an assert fails, your program SHOULD crash.

# That is the idea of assert statement. By failing fast, you reudce the amount
# of code you will have to check before finding the code that is causing the
# problem.
