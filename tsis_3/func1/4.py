def filter_prime(numbers: list):
    primes = list()
    k = 0
    for i in numbers:
        for j in range(2, i):
            if(i % j) == 0:
                break
        else:
            primes.append(i)
    print(primes)




filter_prime([1, 3, 5, 6, 10, 8, 9, 11, 35])