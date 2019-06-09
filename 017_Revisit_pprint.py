# Credit: https://automatetheboringstuff.com/chapter8/
# Revisiting pprint.pformat() function

import pprint
cats = [{'name' : 'Zophie',
         'desc' : 'chubby'},
        {'name' : 'Pooka',
         'desc' : 'fluffy'}]

print('Pretty Format')
print(pprint.pformat(cats))

fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()
