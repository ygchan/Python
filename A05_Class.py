#
# Example file for working with classes
#

# Class are really great way to modulate your program
class myClass():
  # the self argument refer to the object itself, like this in javascript
  def method1(self):
    print("myClass method1")

  def method2(self, someString):
    print("myClass method2 " + someString)

class anotherClass(myClass):
  # the self argument refer to the object itself, like this in javascript
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, someString):
    print("anotherClass method2")

def main():
  # create instance of myClass object
  c = myClass()
  # then you can start calling the functions
  c.method1()
  c.method2("This is a string")

  c2 = anotherClass()
  # invoking myClass method 1 and then anotherClass method 1 print message
  c2.method1() # inherenced method of super class

  c2.method2("Another String") # overwrite the myClass method 2

if __name__ == "__main__":
  main()
