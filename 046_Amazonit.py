# Chapter 11: Web Scraping
# https://automatetheboringstuff.com/chapter11/

#! python3
# amazonit.py - search amazon for a given product

import webbrowser, sys, pyperclip

product = pyperclip.paste()
# search for amazon
# webbrowser.open('https://www.amazon.com/s?k=' + product)

# search for slickdeals
webbrowser.open('https://slickdeals.net/newsearch.php?src=SearchBarV2&q=' + product)
