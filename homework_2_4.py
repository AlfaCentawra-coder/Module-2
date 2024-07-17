numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = ""
not_primes = ""
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    z = 0
    for x in range(1, (len(numbers)+1)):
        if x <= numbers[i]:
            if (numbers[i] % x) == 0:
                z += 1
    if z >= 3:
        not_primes = not_primes + str(numbers[i])
    else:
        primes = primes + str(numbers[i])
print("Простые числа:", primes, "Непростые числа: ", not_primes)