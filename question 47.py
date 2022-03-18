def find_factorization(n):
    se1 = set()
    i = 2
    while i <= n:
        while n % i == 0:
            se1.add(i)
            n = n//i
        i = i + 1
    return len(se1)

def find_mumber(n):
    def check_num(z):
        return find_factorization(z) == n
    h = 2
    counter = 0
    while True:
        print(h)
        h = h + 1
        dummy = check_num(h)
        if dummy == False:
            counter = 0
        if dummy == True:
            counter = counter + 1
            if counter == n:
                return h - n + 1

print(find_mumber(4))






