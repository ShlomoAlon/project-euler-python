MAX = 10000 -1
dic2 = {}
def create_dic(num):
    dic = {}
    for i in range(2,num + 1):
        while i <= num and num % i == 0:
            num = num//i
            try:
                dic[i] = dic[i] + 1
            except:
                dic[i] = 1
        if i >= num:
            return dic


def find_sum(di1 ,number):
    product = 1
    for i in di1:
        product1 = 0
        for z in range(0,di1[i]+1):
            product1 = product1 + i ** z
        product = product * product1
    return product - number

def creat_dic(max):
    for i in range(2,max + 1):
        dic2[i] = find_sum(create_dic(i),i)
    dic2[1] = 1
creat_dic(MAX)
prod = 0
prod1 = 0
print(dic2)
lis = []
for i in dic2:
    prod = dic2[i]
    if dic2[i] < MAX and i != dic2[i] and i == dic2[prod]:
        prod1 = prod1 + i
print(prod1)