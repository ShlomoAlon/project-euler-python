num = 0
for i in range(2,6*(6**9)):
    str1 = str(i)
    product = 0
    for z in str1:
        product = product + int(z)**5
    if product == i:
        num = num + i
        print(i)
        print(num)
print(num)



