# Credit: https://automatetheboringstuff.com/chapter8/
# Revisiting pprint.pformat() function

import pprint
cats = [{'name' : 'Zophie',
         'desc' : 'chubby'},
        {'name' : 'Pooka',
         'desc' : 'fluffy'}]

print('Pretty Format')
pprint.pprint(cats)

print('\nNormal Format')
print(cats)
