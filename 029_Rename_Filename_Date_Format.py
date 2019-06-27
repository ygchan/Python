# https://automatetheboringstuff.com/chapter9/
# Project rename files with American style dates to Eurpoean style dates

# American style = MM-DD-YYYY
# European style = DD-MM-YYYY

# Write program that will handle it for you :)

# Step 01: Search all the filesname in current working directory for AM style
# Step 02: When you found it, swap it to European style.

# Create a regex that can identify the text pattern for AM style dates
# Call os.listdir() to find all the files
# Loop over each filename, using the regex to check weather it has a date
# If it has a date, rename the file with shutil.move()

import shutil, os, re

# Create a regex that matches files with the American date format.
# Passing re.VERBOSE allow white space and comment
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                    # one or two digit for the month
    ((0|1|2|3)?\d)-                # one or two digit for the day
    ((19|20)\d\d)                  # four digits for the year
    (.*?)$                         # all text after the date
    """, re.VERBOSE)               

# To do: Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # To do: From the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # To do: Get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # To do: Rename the files
    # print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    print('Renameing {} to {}...'.format(amerFilename, euroFilename))

    # shutil.move(amerFilename, euroFilename) # uncomment after testing
