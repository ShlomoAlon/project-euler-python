fibonachi_1 = 1
fibonachi_2 = 1
number = 0
while True:
    newfibonachi = fibonachi_1 + fibonachi_2
    fibonachi_2 = fibonachi_1
    fibonachi_1 = newfibonachi
    #print(fibonachi_1)
    if fibonachi_1 >= 4000000:
        break
    elif fibonachi_1 % 2 == 0:
        number = number + fibonachi_1
print(number)

