
def turn_into_palindrome(num):
    num_string = str(num)
    new_num_string = num_string + num_string[::-1]
    return int(new_num_string)


i: int
answer = 0
divisor = 0
for i in range(999,99,-1):
    palindrome = (turn_into_palindrome(i))
    for z in range(999,99,-1):
        if palindrome % z == 0 and palindrome/z < 1000:
            answer = i
            divisor = z
            break
    if answer != 0:
        break
print(answer)
print(divisor)


