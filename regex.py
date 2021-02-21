import re
import sys
# sys.stdin.readline()
texts = "aaaaaaaaa"
pattern = "aa"
match_pattern = re.finditer(pattern,texts)
res = ""
length = 0
for m in match_pattern:
    res += "{0} ".format(m.start() + 1)
    length += 1

print(length)
print(res)

