# Chapter 11: Web Scraping
# https://automatetheboringstuff.com/chapter11/

# What is Web Scraping - using a program to download and process content from
# the internet (Web). In this chapter you will learn the following:
#    - webbrowser - opens a browser to a specific page
#    - Request - download files and web pages from the internet
#    - Beautiful Soup - parses HTML (the format the web pages are written in)
#    - Selenium - lauches and control a web broswer

import webbrowser

# This is about the only thing webbroswer module can do
webbrowser.open('http://inventwithpython.com/')

# George's turn, my favourite website for great deals
webbrowser.open('http://slickdeals.net')
