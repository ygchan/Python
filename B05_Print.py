# create a value here
x = 42

# format is a function of the string object
# not the print function.
print("Hello World. {}".format(x))

# python2 works really differently.
# python2 string wasn't an object, similiar to C

# replace it with the integer value
# this will be removed in future
# please always use python3 format function
print('Hello World. %d' % x)