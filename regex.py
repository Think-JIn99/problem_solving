import re
import sys
# texts = sys.stdin.readline()
# pattern = sys.stdin.readline()
texts = 'banana banana'
pattern = 'ana'
match_pattern = re.finditer(pattern[0],texts)
res = ""
length = 0
for m in match_pattern:
    start = m.start() + 1
    lasts = texts[start:(start - 1 + len(pattern))]
    if lasts != '':
        temp = re.match(pattern[1:],lasts)
        if temp:
            res += "{0} ".format(start)
            length += 1
print(length)
print(res)

