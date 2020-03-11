# Python function always have () even if it does not 
# take arugment. They are not optional.
def function(n = 1):
	print(n)

# passing the value of 47
x = function(47)

# all function return something, in this case None
# the value represent nothing in python.
print(x)