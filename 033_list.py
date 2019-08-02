# To iterate over a list with the numbers

a = ['Python', 'is', 'a', 'great', 'programming', 'lanuage']
for i in range(len(a)):
  print(i, a[i])
  
# Passing a number of strings to a file
# where file is an file object
def write_to_file_many_item(file, separator, *args):
  file.write(separator.join(args))
