def create_identical_list(lis):
    new_lis = []
    for i in lis:
        new_lis.append(i)
    return new_lis

def from_num_to_str(lis):
    new_lis = create_identical_list(lis)
    for i in range(0,len(new_lis)):
        new_lis[i] = str(new_lis[i])
    return new_lis
def from_str_to_num(lis):
    new_lis = create_identical_list(lis)
    for i in range(0, len(new_lis)):
        new_lis[i] = int(new_lis[i])
    return new_lis

def simplify(lis):
    val1 = lis[0]
    val2 = lis[1]
    val1 = int(val1)
    val2 = int(val2)
    for i in range(2,max(val1, val2) + 1):
        while val1 % i == 0 and val2 % i == 0:
            val1 = val1 // i
            val2 = val2 // i
    return [val1,val2]

def cut_same_number(lis):
    new_lis = from_num_to_str(lis)
    se1 = set()
    se2 = set()
    se3 = set()
    for j in new_lis[0]:
        se1.add(j)
    for z in new_lis[1]:
        se2.add(z)
    for h in se1:
        if h in se2:
            se3.add(h)
    for r in se3:
        for i in range(0,2):
            new_lis[i] = new_lis[i].replace(r,'')
    for i in range(0,2):
        if new_lis[i] == '':
            new_lis[i] = '0'
    return from_str_to_num(new_lis)

def check(lis):
    if cut_same_number(lis) != lis and simplify(cut_same_number(lis)) == simplify(lis):
        return True
    else:
        return False

def generate_list(n):
    lis = []
    for i in range(0,n + 1):
        for z in range(0,i):
            lis.append([z,i])
    return lis
def check_lis(lis):
    new_liss = []
    for i in lis:
        if check(i):
            new_liss.append(i)
    return new_liss
def final(n):
    new_lis = check_lis(generate_list(n))
    double_new = []
    for i in new_lis:
        if i[0] % 10 != 0:
            double_new.append(i)
    return double_new
def find_product(lis):
    value1 = 1
    value2 = 1
    for i in lis:
        value1 = value1 * i[0]
        value2 = value2 * i[1]
    return [value1,value2]

print(simplify(find_product(final(100))))






