def triangle(i):
    return (i * (i + 1)) // 2
def pentogonal(i):
    return (i * ((3 * i) - 1)) // 2
def hexoganl(i):
    return (i * ((2 * i) - 1))
def check_in_dic_add_to_counter(dic,i):
    if i in dic:
        dic[i] = dic[i] + 1
    elif i not in dic:
        dic[i] = 1
    return dic
dic = {}
print(check_in_dic_add_to_counter(check_in_dic_add_to_counter(dic,10),10))
print(pentogonal(165))
print(triangle(285))
print(hexoganl(143))


def do_mathy_stuff(n):
    dic = {}
    counter = 0
    i = 1
    while counter < n:
        check_in_dic_add_to_counter(dic,pentogonal(i))
        check_in_dic_add_to_counter(dic,triangle(i))
        check_in_dic_add_to_counter(dic,hexoganl(i))
        if dic[triangle(i)] == 3:
            counter = counter + 1
            print(triangle(i))
        i = i + 1
    return i - 1
print(do_mathy_stuff(3))







