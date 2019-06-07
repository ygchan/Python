# Reference: https://automatetheboringstuff.com/chapter8/
# A program that list the total file size in the folder

import os

totalSize = 0

# os.listdir returns a list for you to loop in
# And at each iteration, you use os.path.join() to create a path&filename
# And then adding it to totalSize
for filename in os.listdir(os.getcwd()):
    totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))

print(totalSize)
