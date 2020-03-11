# While loop

words = ['one', 'two', 'three', 'four', 'five']

n = 0
while (n < 5):
	print(words[n])
	n += 1

# fibonacci series
a, b = 0, 1

while b < 1000:
	print(b, end = ' ', flush = True)
	a, b = b, (a + b)

print() # line ending