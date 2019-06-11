# Credit: https://automatetheboringstuff.com/chapter8/
# Python scripts are just a text file with .py file extension
# The #018 program can even generate other python program

# There is similiarity between SAS include statement and
# python's import statement. #include SAS program is really just another
# text program storing SAS scripts
import myCats

# After you import myCats, all the python code from myCats are "executed"
# or interupted in Python :)

# myCats: The python script filename
# cats: The list that contains dictionary
print(myCats.cats)
print(myCats.cats[0])
print(type(myCats.cats[0])) # Dictionary

# Using the key['name'] to get the value.
print(myCats.cats[0]['name'])
