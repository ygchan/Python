# Credit: https://automatetheboringstuff.com/chapter8/
# Checking out the myCats.py

import pprint

cats = [{'name':'Zophie', 'desc':'chubby'},
        {'name':'Pooka', 'desc':'fluffy'}]

pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
