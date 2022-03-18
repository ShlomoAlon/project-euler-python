def subtract(num1: str, num2: str, base: int):
    lis = []
    answer = ''
    for i in num1:
        lis.append(int(i))
    print(lis)
    for count, letter in enumerate(num2):
        lis[count] -= int(letter)
    for i in range(len(lis)-1,-1,-1):
        if lis[i] < 0:
            lis[i] += base
            lis[i-1] -= 1
    for i in lis:
        answer = answer + str(i)
    return answer
print(subtract('211','112', 2))
def subtract_lis(num1, base):
    answer = sorted(num1)
    for count, elem in enumerate(answer[::-1]):
        answer[count] -= elem
    for i in range(len(num1)-1,-1,-1):
        if answer[i] < 0:
            answer[i] += base
            answer[i-1] -= 1
    return answer















