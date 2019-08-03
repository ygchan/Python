# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

import random
heads = 0

# Simulate a 50/50 coin flip where 1 represents heads
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        # Set the debugger breakpoint here
        print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')

# Summary
# assertion - check if the condition is True, "crash" early so you don't
# have to find out where the code is wrong. Assertion are only for errors
# that the program shouldn't try to recover from and should fail fast.

# exception - using and try and except statements to handle errors gracefully
# and also you can control the display of different level of statement
# without having to worry about removing them after your code is ready.
# And you can also easily write the exception logging to a text file.

# debugger lets you step through program one line at a time, or have it
# runs your program at normal speed and have debugger pause execution at
# breakpoint set. Using a debugger, you can see the state of any variable's
# value at any point during the program's lifetime.
