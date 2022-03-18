num = 6
amount_of_prime_numbers = -1
i = 0
while amount_of_prime_numbers < num:
    i = i + 1
    is_prime = True
    for z in range(2,i):
        if i % z == 0:
            is_prime = False
    if is_prime == True:
        amount_of_prime_numbers = amount_of_prime_numbers + 1
print(amount_of_prime_numbers)
print(i)