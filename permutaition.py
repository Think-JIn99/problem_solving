import copy
def permutaition(num_list,remved_num):
    if len(num_list) == 1:
        print(f"{remved_num}{num_list}", end = '')
        return

    for i in num_list:
        list_copy = copy.deepcopy(num_list)
        permutaition(list_copy.remove(i),remved_num + i)
        print('')

num_list = int(input())
permutaition(list(range(1,num_list + 1)),0)
