num = 2000000
list_of_number = [True]*(num)
print(list_of_number)
for i in range(2,num):
    if list_of_number[i-1] == True:
        for z in range(i * 2,num, i):
            print(i)
            print(z)
            list_of_number[z-1] = False
product = 0
for x in range(0,len(list_of_number)-1):
    if list_of_number[x] == True:
        product = product + x + 1

print(product - 1)