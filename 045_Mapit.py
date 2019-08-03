# Chapter 11: Web Scraping
# https://automatetheboringstuff.com/chapter11/

# Useful program to lauch a map
# Get a street address from the command line arugment/clipboard
# Open the web browser to the Google Map page for the address

# Need to read the command line arugments from sys.argv
# Read the clipboard contents
# Call the webbroswer.open() function to open the web broswer

# Sample usage: mapit 100 church street, NY, NY 10003
# If there are no arugment in the command line, the program will use 

# Your program can be set to open a web browser to
# 'https://www.google.com/maps/place/your_address_string'

#! python3
# mapIt.py - Lauches a map in the browser using an address from the
# command line or clipboard

# Chapter 11: Web Scraping
# https://automatetheboringstuff.com/chapter11/

# Useful program to lauch a map
# Get a street address from the command line arugment/clipboard
# Open the web browser to the Google Map page for the address

# Need to read the command line arugments from sys.argv
# Read the clipboard contents
# Call the webbroswer.open() function to open the web broswer

# Sample usage: mapit 100 church street, NY, NY 10003
# If there are no arugment in the command line, the program will use 

# Your program can be set to open a web browser to
# 'https://www.google.com/maps/place/your_address_string'

#! python3
# mapIt.py - Lauches a map in the browser using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])

    # sys.argv[0] is your program's filename
    print(address)

else:
    # Get address from clipboard
    address = pyperclip.paste()

    
webbrowser.open('https://www.google.com/maps/place/' + address)
