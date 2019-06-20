# Reference: https://automatetheboringstuff.com/chapter9/
import os

# Looping each file in that directory
for filename in os.listdir():
    # endswith allows you to check for last few characters
    if filename.endswith('.rxt'):
        # Should at least print out the name to confirm first!
        print(filename)
        # And only after you may delete it :)
        # os.unlink(filename)
