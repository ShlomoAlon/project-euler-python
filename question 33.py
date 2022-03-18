def create_list_of_fractions(n):
    lis = []
    for i in range(0,n + 1):
        for z in range(0,i):
            lis.append([str(z),str(i)])
    return lis
def find_common_digits(lis1):
    set1 = set()
    set2 = set()
    set3 = set()
    print(lis1)
    for i in lis1[0]:
        print(i)
        set1.add(i)
    for z in lis1[1]:
        set2.add(z)
    for i in set1:
        if i in set2:
            set3.add(i)
    return set3
def cancel_out(lis1):
    list2 = []
    print(lis1)
    for i in lis1:
        print(i)
        print(list2)
        list2.append(i)
    print(list2)
    set1 = find_common_digits(list2)
    for i in range(0,2):
        for j in list2[i]:
            if j in set1:
                list2[i] = list2[i].replace(j,'')
    return list2
print(cancel_out(['15','10']))

def return_value(lis1):
    if '' in lis1:
        return lis1
    value1 = int(lis1[0])
    value2 = int(lis1[1])
    for i in range(2,value2):
        while value1 % i == 0 and value2 % i == 0:
            value1 = value1 // i
            value2 = value2 // i
    return [value1,value2]

def check(lis1):
    print(lis1)
    print(return_value(lis1))
    print(lis1)
    print(return_value(cancel_out(lis1)))
    print(lis1)
    print(cancel_out(lis1))
    return return_value(lis1) == return_value(cancel_out(lis1)) and cancel_out(lis1) != lis1

print(check(['49', '98']))

def full_check(lis1):
    new_lis = []
    for i in lis1:
        if check(i):
            new_lis.append(i)
    return new_lis
new_lis = (full_check(create_list_of_fractions(100)))
second_lis = []
for item in new_lis:
    if int(item[0]) % 10 != 0:
        print(item)
        second_lis.append(item)

product1 = 0
prodcut2 = 0
for item in second_lis:
    product1 = int(item[0]) + product1
    prodcut2 = int(item[1]) + prodcut2
print(product1,prodcut2)
print(return_value([str(product1),str(prodcut2)]))












