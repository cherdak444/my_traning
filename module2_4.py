from os import remove
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    for j in range(2, numbers[i]):
        if numbers[i] % j > 0:
            is_prime = True
            continue
        else:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    elif is_prime == False:
        not_primes.append(numbers[i])
primes.remove(1)
print(primes)
print(not_primes)
