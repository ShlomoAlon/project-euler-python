dic = {}
dic[1] = 1
def collatz(num):
    if num in dic:
        return dic[num]
    if num % 2 == 0:
        dic[num] = collatz(num // 2) + 1
    else:
        dic[num] = collatz(num * 3 + 1) + 1
    return dic[num]
for i in range(2,1000001):
    collatz(i)
key = 0
max = 0
for i in dic:
    if dic[i] > max:
        key = i
        max = dic[i]
print(key,max)

