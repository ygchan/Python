# Credit: https://automatetheboringstuff.com/chapter8/
# Checking out the myCats.py

import pprint

cats = [{'name':'Zophie', 'desc':'chubby'},
        {'name':'Pooka', 'desc':'fluffy'}]

pprint.pformat(cats)
fileObj = open('myCats.py', 'w')

# Using pprint.pformat to look like on one line
# And then putting the myCats list into a py write.
# Writing it line by line
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
