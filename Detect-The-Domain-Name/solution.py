import re

regex_pattern = r"https?://[a-z+0-9\.\-]{1,}[a-z]{2,3}"

N = int(raw_input())
outputs = []

for i in range(N):
    S = raw_input()
    result = re.findall(regex_pattern, S)
    outputs.append(result)

# strip empty matches
outputs_clean = [i for i in outputs if i != []]

# flat the list
outputs_clean = [item for sublist in outputs_clean for item in sublist]

# avaoid all matches which don't have at least one dot
outputs_clean = [i for i in outputs_clean if '.' in i]

# strip www and http:// prefixes:
outputs_clean = [i.replace('www.', '') for i in outputs_clean]
outputs_clean = [i.replace('http://', '') for i in outputs_clean]
outputs_clean = [i.replace('https://', '') for i in outputs_clean]

outputs = []
[outputs.append(i) for i in outputs_clean if i not in outputs]
outputs.sort()
print ';'.join(outputs)
