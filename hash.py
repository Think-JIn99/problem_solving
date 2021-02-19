size = int(input())
strigns = list(input())
val = 0
sum = 0
for i in range(size):
    val = ((ord(strigns[i])-96)*pow(31,i))
    sum += val
print(sum % 1234567891)