def is_right_triangle(x,y,z):
    return x ** 2 + y ** 2 == z ** 2
def return_sum(x,y,z):
    return x + y + z
def create_dic(num):
    dic = {}
    for i in range(1,num + 1):
        dic[i] = 0
    for z in range(1,num):
        for y in range(1,z):
            for x in range(1,y + 1):
                dummy = return_sum(x,y,z)
                if dummy <= num and is_right_triangle(x,y,z):
                    dic[dummy] = dic[dummy] + 1



    return dic
dic = create_dic(1000)
print(dic)
print(max(dic, key=dic.get))


