# Credit: https://automatetheboringstuff.com/chapter8/

import shelve

# Loading a binary shelve file
shelfFile = shelve.open('mydata')

# This object is class 'shelve.DbfilenameShelf'
print(type(shelfFile))

# And you also have the cats list
# When you print it shows a memory address?
print(shelfFile)

# But you can access the list.
print(shelfFile['cats'])

# Similiar to a dictionary, shelve is like a dictionary
# it has keys() and values()

print(list(shelfFile.keys()))
print(list(shelfFile.values()))

# Good habit to close it
shelfFile.close()

# Plaintext is useful for creating a data extract, but if you want to save
# "data" from a program run, or maybe like a "state" of your program.
# Then shelve module is an excellent tool. :)

# Recap: import shelve to allow using shelve module
# You can save an object using
# shelfFile = shelve.open('myData') << This create an binary shelve file
# shelfFile['name'] = object        << object is what you want to store

# if you want to load it back
# shelfFile = shelve.open('myData')
# object = shelFile['name']         << This gives back what you stored.

# As usual, always close them
# shelfFile.close()
