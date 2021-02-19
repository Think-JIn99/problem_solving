table = [0 for i in range(0,100000)]
n = input()
keys = list(map(int,input().split()))
m = input()
compare = list(map(int,input().split()))

for k in keys:
    idx = k % len(table)
    if not table[idx]:
        table[idx] = 1

for c in compare:
    idx = c % len(table)
    print(table[idx])