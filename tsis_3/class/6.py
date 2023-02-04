import math
nums = range(0, 100)

primes = filter(lambda x : all(x > 0 and x % i != 0 for i in range(2, round(math.sqrt(x) + 1))), nums)
primes = list(primes)
print(primes)