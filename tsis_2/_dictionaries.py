thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
x = thisdict.get("model")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# The pop() method removes the item with the specified key name:
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
# The del keyword removes the item with the specified key name:
# The clear() method empties the dictionary:

for x in thisdict:
  print(x, end=" ") 

thisdict =	{ # Make a copy of a dictionary with the copy() method:
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 

print(myfamily)