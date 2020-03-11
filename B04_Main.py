# A block is delimited by indents

import platform

def main():
	message()

# A block is indicated by common indentations.
def message():
	print("This is python version {}".format(platform.python_version()))
	print("Same level")
	print("Still writing")
print("This line is first")

if __name__ == "__main__": main()