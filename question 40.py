def create_str(n):
    i = 1
    str1 = ''
    while len(str1) < n:
        str1 = str1 + str(i)
        i = i + 1
    return str1
print(create_str(12))
def find_index(str1,n):
    return int(str1[n - 1])
print(find_index(create_str(12),10))
def product(n):
    str1 = create_str(n + 1)
    pro = 1
    i = 10
    while i < n:
        pro = pro * find_index(str1,i)
        i = i * 10
    return pro
print(product(1000000))