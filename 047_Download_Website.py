# Chapter 11: Web Scraping
# https://automatetheboringstuff.com/chapter11/

# Download a web page
import requests

# Response object
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# <class 'requests.models.Response'>
print(type(res))

# Making sure it is loaded (avaliable)
print(res.status_code == requests.codes.ok)

# .text are the data
print(len(res.text))

# you can slice the data
# print(res.text[:250])

# Let's find out the words frequency!
word_dict = {}

# Create a little word dictionary
# https://stackoverflow.com/a/1692428
for word in res.text.split():
    word = word.lower().strip()
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 0

number_of_result = 20

# How to sort a dictionary and print top results
# https://stackoverflow.com/a/3177911
for word in sorted(word_dict, key=word_dict.get, reverse=True):

    # Left justify: https://stackabuse.com/formatting-strings-with-python/
    print('{0:<5}: {1:<5}'.format(word, word_dict[word]))
    number_of_result -= 1
    if number_of_result == 0:
        break
