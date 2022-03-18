def is_pan_digital(str1):
    set1 = set(range(1, len(str1)+1))
    set2 = set()
    for i in str1:
        set2.add(int(i))
    if set1 != set2:
        return False
    else:
        return True
def return_string_of_multiples(num,num1):
    return str(num) + str(num1) + str(num1*num)
setties = set()
for i in range(1,2000):
    for z in range(1,2000):
        if len(str(i)) + len(str(z)) + len(str(i * z)) == 9 and is_pan_digital(return_string_of_multiples(z,i)):
            setties.add(i*z)
            print(i,z)
            print(i*z)
sum = 0
for i in setties:
    sum = sum + i
print(sum)
