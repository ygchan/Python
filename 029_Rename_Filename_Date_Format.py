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
datePatter = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                    # one or two digit for the month
    ((0|1|2|3)?\d)-                # one or two digit for the day
    ((19|20)\d\d)                  # four digits for the year
    (.*?)$                         # all text after the date
    """, re.VERBOSE)

# To do: Loop over the files in the working directory

# To do: skip files without a date

# To do: Get the different parts of a filename

# To do: From the European-style filename

# To do: Get the full, absolute file paths

# To do: Rename the files
