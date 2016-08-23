import sys
import re

N = int(raw_input())
lines = []

for i in xrange(N):
    s = raw_input()
    lines.append(s)
    
print ';'.join(sorted(list(set(re.findall(r"(?<=<)[a-z0-9]+", ' '.join(lines))))))