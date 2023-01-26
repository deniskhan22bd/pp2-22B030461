#Python Arithmetic Operators
x, y = 3, 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)
print(x % y)

#Operator is, it not, in, in not 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]

print("pineapple" not in x) # returns True because a sequence with the value "pineapple" is not in the list
print("banana" in x) # returns True because a sequence with the value "banana" is in the list

