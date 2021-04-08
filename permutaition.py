import copy
def permutaition(num_list,removed_nums):
    if len(num_list) == 1:
        print(removed_nums + num_list)
        return

    for i in num_list:
        list_copy = copy.deepcopy(num_list)
        permutaition(list_copy.replace(i,''), removed_nums + i + " ")

num_list = [str(i) for i in range(1 , int(input()) + 1)]
num_list = ''.join(num_list)
permutaition(num_list,"")
