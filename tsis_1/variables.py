x = 4  # int
y = "Hello World!" # string
z = 3.5 # float
w = True # bool



x = y = z = "Orange"
print(x)
print(y)
print(z)

print()
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print()
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 