def generage_list_of_primes(n):
    lis = [True] * (n + 1)
    lis[0] = False
    lis[1] = False
    for i in range(0,n + 1):
        if lis[i]:
            for h in range(2*i,n + 1,i):
                lis[h] = False
    primes = []
    for z in range(0,n + 1):
        if lis[z] == True:
            primes.append(z)
    return primes
def create_list(lis):
    se1 = set(lis)
    lis1 = []
    def check_left(n):
        dummy = str(n)
        while dummy != '':
            if int(dummy) in se1:
                dummy = dummy[1:]
            else:
                return False
        return True
    def check_right(n):
        dummy = str(n)
        while dummy != '':
            if int(dummy) in se1:
                dummy = dummy[:-1]
            else:
                return False
        return True
    for i in lis:
        if check_right(i) and check_left(i) and i > 10:
            lis1.append(i)
    return lis1

def sum_of_lis(lis):
    sum = 0
    for i in lis:
        sum = sum + i
    return sum
print(sum_of_lis(create_list(generage_list_of_primes(1000000))))
