import re
strings = "ABC ABCDAB ABCDABCDABDE"
match_pattern = "ABCDABD"
print(len(re.findall(match_pattern,strings)))
for matched in re.finditer(match_pattern,strings):
    print(matched.start() + 1)
