num = 10001
list_of_primes =[]
i = 1
while len(list_of_primes)<num:
    i = i + 1
    is_prime = True
    for z in list_of_primes:
        if i % z == 0:
            is_prime = False
            break
    if is_prime == True:
        list_of_primes.append(i)


print(list_of_primes)
print(list_of_primes[-1])
