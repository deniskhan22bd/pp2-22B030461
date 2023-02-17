#1
"""
n = int(input())

def squares(n: int):
    for i in range(1, n):
        yield i ** 2

a = squares(n)

for i in a:
    print(i)
"""

#2
"""
n = int(input())

def even(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

evens = list()
for i in even(n):
    evens.append(str(i))

print(", ".join(evens))
"""

#3
"""
n = int(input())

def div(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for i in div(n):
    print(i, end= " ")
"""

#4
"""
a = int(input())
b = int(input())

def squares(a, b):
    for i in range(a, b):
        yield i ** 2

for i in squares(a, b):
    print(i)
"""

#5
"""
n = int(input())

def nums(n):
    for i in range(n, 0, -1):
        yield i

for i in nums(n):
    print(i)
"""