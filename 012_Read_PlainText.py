# Reference: https://automatetheboringstuff.com/chapter8/
# Open() function takes a string path, it can be relative/absolute
import os

currentDir = os.getcwd()
filePath = os.path.join(currentDir, 'hello.txt')

# Reading plaintext mode, or read mode for short
# it returns a file object
hellofile = open(filePath)

# Or you can specify it by passing 'r' as second argument to open()
# hellofile = open(filePath, 'r')

oneLine = hellofile.readlines()
print(oneLine)

hellofile.close()
