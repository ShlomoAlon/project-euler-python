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
def check_if_has_zero(n):
    for z in (0,2,4,6,5,8):
        if str(z) in str(n):
            return False
        else:
            return True

def create_set_of_circulars(lis):
    se1 = set(lis)
    counter = 0
    for i in se1:
        lis = []
        if check_if_has_zero(i) == True:
            lis.append(i)
            dummy = str(i)
            dummy = dummy[1: ] + dummy[0]
            for z in range(1,len(str(i))):
                if int(dummy) in se1:
                    lis.append(int(dummy))
                else:
                    break
                dummy = dummy[1:] + dummy[0]
            if len(lis) == len(str(i)):
                print(lis)
                counter = counter + 1
    return counter


print(create_set_of_circulars(generage_list_of_primes(1000000)))




