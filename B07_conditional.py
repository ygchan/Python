# conditional statment

x = 42
y = 73

# python does not have switch statement
# if, elif, else

if x > y:
	print("x > y: x is {} and y is {}".format(x, y))
elif x < y:
	print("x < y: x is {} and y is {}".format(x, y))
elif x == y:
	print("x == y: x is {} and y is {}".format(x, y))
else:
	print('do something else')