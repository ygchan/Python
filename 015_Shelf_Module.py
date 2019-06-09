# Credit: https://automatetheboringstuff.com/chapter8/
# If you run a program and entered some configuration settings,
# you can save these into a binary shelf file and interact with them later.
import shelve

# Create a binary shelf file using shelve module
shelfFile = shelve.open('mydata')
cats = ['Zohpie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

# To read and write data using the shlve,
# simply shelve.open() ...
# and it turns a varaible that you are looking for.
