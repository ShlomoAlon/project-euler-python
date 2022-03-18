MAX_NUM = 28123
def return_sum_of_proper_divisors(num):
    """takes in a integer and returns the sum of divisors"""
    def create_dic_of_prime_divisors(num1):
        """takes in a number and returns a dictionary that counts how many time a prime divisor occurs"""
        dic = {}
        for i in range(2,num1 + 1):
            while i <= num1 and num1 % i == 0:
                num1 = num1//i
                try:
                    dic[i] = dic[i] + 1
                except:
                    dic[i] = 1
        return dic
    def find_sum(dic1):
        """takes in a dictionary and calculates the sum of divisors"""
        product = 1
        for i in dic1:
            product1 = 0
            for z in range(0,dic1[i] + 1):
                product1 = product1 + i**z
            product = product * product1
        return product - num
    return find_sum(create_dic_of_prime_divisors(num))


def find_sum_of_all_sums_of_abundant_numbers(n):
    def create_list_of_abundant_numbers(n1):
        """takes in integer and returns of a list of all numbers that are abundant that are smaller then it"""
        lis = []
        for i in range(10,n1):
            if return_sum_of_proper_divisors(i) > i:
                lis.append(i)
        return lis
    def create_dic_of_sum_of_two_abundant_numbers(lis):
        """takes in a list and creates a dictionary of the sum of the items of list that are less then n"""
        dic = {}
        for i in lis:
            for z in lis:
                if i + z <= n:
                    dic[i + z] = i + z
        return dic
    def find_sum_of_all_sums_in_dic(dic):
        product = 0
        for i in range(0,n):
            if i not in dic.keys():
                product = i + product
        return product

    print(create_list_of_abundant_numbers(n))
    print(create_dic_of_sum_of_two_abundant_numbers(create_list_of_abundant_numbers(n)))
    print(find_sum_of_all_sums_in_dic(create_dic_of_sum_of_two_abundant_numbers(create_list_of_abundant_numbers(n))))
    return find_sum_of_all_sums_in_dic(create_dic_of_sum_of_two_abundant_numbers(create_list_of_abundant_numbers(n)))
print(find_sum_of_all_sums_of_abundant_numbers(MAX_NUM))



