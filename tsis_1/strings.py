b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[-5:-2])

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 


txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.") 

a = "Hello, World!"
print(len(a))

for x in "banana":
    print(x) 