#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  # while loop execute while the condition is True
  while (x < 5):
    print(x)
    x = x + 1

  # define a for loop
  # There is no index counter variable
  # Python loops are iterators, use the range to return the range of numbers
  # 10 is not inclusive in the range, this prints out 5-9
  for x in range(5, 10):
    print(x)

  # use a for loop over a collection
  # At each iteration it will loop through the content of the list
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for d in days:
    print(d)
 
  # use the break and continue statements
  # New way of using the break statement within this line!
  for x in range(5, 10):
    # if (x == 7): break
    # if x divide by 2, remainder is 0, don't print x
    # skipping 6, 8
    if (x % 2 == 0): continue
    print(x)

  #using the enumerate() function to get index 
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i, d in enumerate(days):
    # return the index of collection and member of collection
    print(i, d)


if __name__ == "__main__":
  main()
