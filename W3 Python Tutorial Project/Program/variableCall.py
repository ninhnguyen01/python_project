# Global Variables
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  # variable x here is a local scope (only accessible within the function)    
  x = "fantastic"
  print("Python is " + x)
  
myfunc() 
# print statment below access the global scope
print("Python is " + x)

def newfunc():
  global y
  y = "cool"
  print("Python is " + y)

newfunc()