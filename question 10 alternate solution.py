num = 2000000
list_of_numbers = []
for i in range(2, num + 1):
    list_of_numbers.append(i)
i = -1
while True:
    i = i + 1
    if i == len(list_of_numbers)-1:
        break
    divisor = list_of_numbers[i]
    god = 0
    for z in range(i + 1,len(list_of_numbers)):
        new_number = list_of_numbers[z - god]
        if new_number % divisor == 0:
            print(list_of_numbers[z - god])
            list_of_numbers.pop(z - god)
            god = god + 1

print(list_of_numbers)




