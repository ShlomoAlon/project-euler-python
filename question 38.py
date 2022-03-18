def is_pandigtal9(str1):
    if len(str1) != 9:
        return False
    se1 = set()
    for i in range(1, 10):
        se1.add(str(i))
    for i in se1:
        if i not in str1:
            return False
    return True
def create_string(num):
    str1 = ''
    for i in range(1,6):
        str1 = str1 + str(num * i)
        if len(str1) >= 9:
            break
    return str1
print(is_pandigtal9(create_string(112)))

def largest_pandigtal():
    largest = 0
    for i in range(1,9999):
        if is_pandigtal9(create_string(i)):
            if int(create_string(i)) > largest:
                largest = int(create_string(i))
    return largest
print(largest_pandigtal())


