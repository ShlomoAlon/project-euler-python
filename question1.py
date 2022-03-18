number: int = 0
import icecream

for i in range(1,100000000):
    if i % 5 == 0:
        number = number + i
    elif i % 3 == 0:
        number = number + i
print(number)

def better_code(n):
    sum = 0
    for i in range(3,n,3):
        sum = sum + i
    for i in range(5,n,5):
        sum = sum + i
    for i in range(15,n,15):
        sum = sum - i
    return sum
print(better_code(100000000))



