num = 20
dic = {}
dic[num,num] = 1
def check_moves(x,y):
    if (x,y) in dic:
        return dic[x,y]
    num_moves = 0
    if x < num:
        num_moves = num_moves + check_moves(x + 1, y)
    if y < num:
        num_moves = num_moves + check_moves(x, y + 1)
    dic[x,y] = num_moves
print(dic)



for x in range(num,-1,-1):
    for y in range(num,-1,-1):
        check_moves(x,y)
print(dic)