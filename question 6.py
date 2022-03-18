num = 100
factorial_of_num = (num * (num + 1)) / 2
print(factorial_of_num)
square_of_sum = factorial_of_num ** 2
print(square_of_sum)
sum_of_squares = 0
for i in range(1,num + 1):
    sum_of_squares = sum_of_squares + (i ** 2)
print(sum_of_squares)
diference = square_of_sum - sum_of_squares
print(diference)

