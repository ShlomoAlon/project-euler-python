def is_valid_integer(n):
    """takes in a integer and checks if it has any doubles and that it is smaller then largest possible number"""
    dic = {}
    for i in str(n):
        if int(i) in dic:
            return False
        else:
            dic[int(i)] = 1
    return True
def create_count_of_valid_integers(n):
    num_of_valid = 0
    for i in range(123456789,9876543211):
        if is_valid_integer(i):
            num_of_valid = num_of_valid + 1
        if num_of_valid == n:
            return i
print(create_count_of_valid_integers(1000000))

