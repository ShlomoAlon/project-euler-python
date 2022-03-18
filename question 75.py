import math
def is_triplet(x,y):
    return int(math.sqrt(x ** 2 + y ** 2)) == math.sqrt(x ** 2 + y ** 2)
def create_dic(n):
    dic = {}
    for i in range(1,n):
        print(i)
        for z in range(1, i + 1):
            if is_triplet(i,z):
                dummy = i + z + int(math.sqrt(i ** 2 + z ** 2))
                if dummy in dic:
                    dic[dummy] = dic[dummy] + 1
                else:
                    dic[dummy] = 1
    return dic
print(create_dic(1500000))
