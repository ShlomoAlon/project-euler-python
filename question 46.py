import math
def array_of_primes(n):
    arr = [True] * n
    for i in range(2,n):
        if arr[i] == True:
            for z in range(2 * i,n,i):
                arr[z] = False
    return arr


def lis_of_odd_composite_numbers(n):
    lis = array_of_primes(n)
    new_lis = []
    for i in range(1,len(lis),2):
        if lis[i] == False:
            new_lis.append(i)
    return new_lis
def create_lis_of_primes(n):
    lis = array_of_primes(n)
    new_lis = []
    for i in range(2,len(lis)):
        if lis[i] == True:
            new_lis.append(i)
    return new_lis
def goldbach(n):
    composite = lis_of_odd_composite_numbers(n)
    primes = create_lis_of_primes(n)

    def check_num(i):
        for z in primes:
            print(z)
            print(i)
            if z > i:
                return False
            elif math.sqrt((i - z)/ 2) == int(math.sqrt((i - z)/2)):
                return True
    for h in composite:
        if check_num(h) == False:
            return h
goldbach(10000000)
