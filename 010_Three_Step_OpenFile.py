# Reference: https://automatetheboringstuff.com/chapter8/
# A reading before bedtime about how to read a python file.

# Step #01. Call open() function to return a file object
# Step #02. Call the read() function on the file object
# Step #03. Call the close() function on the file object

# This is a practice program to read the source code

# Open the file as f (file object) named f.
with open('/Users/Study/Python/002_Date_Cleanup.py', 'r') as f:
    # Loop it by line
    for line in f:
        # If after stripping the newlines still not blank
        if len(line.strip()) > 1:
            # Print (but remove the new line
            print(line.rstrip())

# Always remember to close the file :)
f.close()
