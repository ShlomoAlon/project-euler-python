import math
sum = 0
i = 2
while True:
    i = i + 1
    str1 = str(i)
    product = 0
    for z in str1:
        product = product + math.factorial(int(z))
    if product == i:
        sum = sum + i
        print(sum)


