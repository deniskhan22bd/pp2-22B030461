fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end= " ")

print()

for x in "banana":
  print(x, end= " ")

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x, end= " ")
  if x == "banana":
    break

print() 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x, end= " ")

print()


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x, end= " ")

print()

for x in range(2, 30, 3): #first value - start, second - last, third - step, [2, 30)
  print(x, end= " ")

print()

for x in range(6):
  print(x , end= " ")
else:
  print("\tFinally finished!") 

print()


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y,"\n") 

print()



