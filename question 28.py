amount_to_skip = 2
number = 1
sum = 1
lis = []
while len(lis) / 2 < 1000:
    for z in range(0,4):
        number = number + amount_to_skip
        lis.append(number)
    amount_to_skip = amount_to_skip + 2
    print(amount_to_skip)
print(lis)
for i in lis:
    sum = sum + i
print(sum)

