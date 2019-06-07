# Reference: https://automatetheboringstuff.com/chapter8/
# A program that check if a folder/file exits

import os

my_good_file = '/Users/Study/Python/002_Date_Cleanup.py'
my_bad_file = '/Users/Study/Python/002_dummy.py'

print(my_good_file + 'exists? -- ' + str(os.path.exists(my_good_file)))
print(my_bad_file + ' exists? -- ' + str(os.path.exists(my_bad_file)))

# isfile - check if a file exits, return bool value
# isdir  - check if a dir exits, return bool value too.
