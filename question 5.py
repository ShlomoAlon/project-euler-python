def check_if_divisible(num,max):
    for i in range(2,max + 1):
        if num % i != 0:
            return False
    return True
print(check_if_divisible(6,3))
num = 20
i = num
while True:
    i = i + num
    if check_if_divisible(i,num) == True:
        print(i)
        break
