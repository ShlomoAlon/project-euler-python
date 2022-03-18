MAX = 1000
f1 = 1
f2 = 1
i = 2
while True:
    i = i + 1
    new = f1 + f2
    f2 = f1
    f1 = new
    print(i,f1)
    if len(str(f1)) == MAX:
        print(i)
        break

