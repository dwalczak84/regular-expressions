import re
regex_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"
N = int(raw_input())

for i in range(N):
    S = raw_input()
    if bool(re.search(regex_pattern, S)) and len(S) == 10:
        print 'YES'
    else:
        print 'NO'