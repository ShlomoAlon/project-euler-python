lis = []
for i in range(2,101):
    for z in range(2,101):
        if i ** z not in lis:
            lis.append(i**z)
print(len(lis))
