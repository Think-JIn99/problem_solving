#백준 1920
table = [[] for i in range(0,100000)]
n = input()
keys = list(map(int,input().split()))
m = input()
compare = list(map(int,input().split()))

for k in keys:
    idx = k % len(table)
    table[idx].append(k)

for c in compare:
    idx = c % len(table)
    find = False
    for val in table[idx]:
        if val == c:
            # print("idx: {0} val: {1}".format(idx,val))
            print(1)
            find = True
            break

    if not find:
        print(0)