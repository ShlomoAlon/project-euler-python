num = 16
for i in range(1,num):
    for z in range(2, num):
        if num % z == 0:
            num = int(num / z)
            print(num)
            break
print(num)
