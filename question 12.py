def dic_prime_divisors(n):
    """ this function takes in a number and outputs its divisors in dictionary form"""
    dic1= {}
    i = 1
    while True:
        i = i + 1
        while n % i == 0 and i <= n:
            n = n / i
            if i in dic1:
                dic1[i] = dic1[i] + 1
            else: dic1[i] = 1
        if i >= n:
            break
    return dic1
def how_many_divisors(dic1):
    product = 1
    for i in dic1.values():
        product = product * (i + 1)
    return product


def main(num):
    i = 1
    triangle = 1
    while True:
        i = i + 1
        triangle = triangle + i
        if how_many_divisors(dic_prime_divisors(triangle)) >= num:
            return triangle
print(main(500))

