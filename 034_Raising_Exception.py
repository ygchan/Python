# Chapter 10: Debugging
# https://automatetheboringstuff.com/chapter10/

# There are a few tools to help you identify exactly what your code is doing
# and where it is has gone wrong.

# 1. Look at logging and assertions
# They both help you detect bugs early.

# Generally, the earlier you catch the bugs, the easier they will be to fix

# 2. Learn how to use the debugger, it is a feature of the IDLE that execute
# a program one instruction at a time. Giving you a chance to inspect the value
# in the program while your code runs. (Does it mean it print(myvar) for you?

# Running code in debugger is slower, but it's a good thing!
# Python raises an exception whenever it tries to execute invalid code

# try & except statement
# they allow your program to recover from exceptions that you anticipated.

# Raising an exception is a way to "stop running the code, and move the
# program execution to the except statement.
#   - raise keyword
#   - Exception function
#   - string with helpful error message

# raise Exception('This is the error message!')

# Using the try and except statements, you can handle the errors more
# gracefully instead of letting the entire program crash.

def boxPrint(symbol, width, height):
    '''Take a character, width and height to make a little box'''
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

# A tuple of tuples unpacking in for loop
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))

# Practicing try and except method
def namePrint(name):
    '''Take a string and print it to the screen'''
    if not (name.isalpha()):
        raise Exception('Name must contain only letters')
    print('Hello', name.title())

while True:
    buffer = input('What is your name (q to exit): ')
    if buffer == 'q':
        break
    try:
        namePrint(buffer)
    except Exception as err:
        print('An exception happened: ' + str(err))
        
