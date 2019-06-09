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

# Good habit to close it
shelfFile.close()
