answer = 0
for a in range(1,1000):
    for b in range(a,1000-a+1):
        for c in range(b,1000-a-b+1):
            if a**2 + b**2 == c**2:
                print(a+b+c)
                if a + b + c == 1000:
                    answer = (a * b* c)
                    break

print(answer)

