thisset = {"apple", "banana", "cherry"}
print(thisset) 

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset)) 
set1 = {"abc", 34, True, 40, "male"} # containg different data types
print(type(thisset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

thisset = {"apple", "banana", "cherry"} # add set to set
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

thisset = {"apple", "banana", "cherry"} # update for any data stores
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) 

thisset = {"apple", "banana", "cherry"} # remove
thisset.remove("banana")
print(thisset) 

thisset = {"apple", "banana", "cherry"} # remove by discard
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"} # pop, deleting the random el
x = thisset.pop()
print(x)
print(thisset) 

thisset = {"apple", "banana", "cherry"} # loop
for x in thisset:
  print(x) 
 
set1 = {"a", "b" , "c"} # join sets by union()
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) 

x = {"apple", "banana", "cherry"} # The intersection_update() method will keep only the items that are present in both sets.
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"} # The intersection() method will return a new set, that only contains the items that are present in both sets.
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 

x = {"apple", "banana", "cherry"} # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x) 

x = {"apple", "banana", "cherry"}# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) 

"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""