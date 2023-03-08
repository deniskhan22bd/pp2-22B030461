import math
import time
#1.1
"""
nums = [13, 5, 613, 5, 31, 4, 5, 6]
print(math.prod(nums))
"""

#1.2
"""
nums = [13, 5, 613, 5, 31, 4, 5, 6]
prod = 1
for i in nums:
    prod *= i
print(prod)
"""

#2
"""
upper = 0 
lower = 0
s = input()
for i in s:
    if i == i.lower():
        lower += 1
    else:
        upper += 1
print(upper, lower)
"""

#3
"""
s = input()
if s == s[::-1]:
    print("it's palindrome")
else:
    print("it's not")
"""

#4
"""
n = int(input())
t = int(input())
time.sleep(t / 1000)
print(f"Square root of {n} after {t} miliseconds is {math.sqrt(n)}")
"""

#5
"""
tup = (True, 13513, "5315")
print(all(tup))
tup = (True, 1351, "r31", False)
print(all(tup))
"""