num = 100
def get_factorial(num1):
    factorial = 1
    for i in range(1,num1+1):
        factorial = factorial * i
    return factorial

def sum_of_digits(num2):
    st1 = str(num2)
    sum = 0
    for i in st1:
        sum = sum + int(i)
    return sum
print(sum_of_digits(get_factorial(num)))

