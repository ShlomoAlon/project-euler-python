num = 10
list_of_primes = []
print(list_of_primes)
for i in range(2,num + 1):
    is_prime = True
    for z in list_of_primes:
        if i % z == 0:
            is_prime = False
            break
    if is_prime == True:
        list_of_primes.append(i)
        print(list_of_primes[-1])
sum_of_primes = 0
for i in list_of_primes:
    sum_of_primes = sum_of_primes + i
print(sum_of_primes)
