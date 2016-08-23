import sys
import re
import string

# regex patterns:
regex_pattern_for_attributs = r"(?<=\s{1})[a-z0-9]+\="
regex_pattern_for_tags = r"<[a-z0-9]+"
regex_pattern = r"[a-z0-9=]+|\>|\<"

# create one global list for input:
input_global = []

# create one output list for further input_global processing:
output2 = []

# read data:
N = int(raw_input())
for i in range(N):
    S = raw_input()
    output2.extend(re.findall(regex_pattern, S))
    input_global.append(S)
    
input_global = ' '.join(input_global)

# finding unique tags in input:
output_tags = list(set([i.replace('<', '') for i in re.findall(regex_pattern_for_tags, input_global)]))

# finding unique attributes in input, kep '=' for the next processing:
output_attributes = list(set([i for i in re.findall(regex_pattern_for_attributs, input_global)]))

# finding every tag and attribute in input_global string
output3 = []

for i in output2:
    if i in output_attributes or i == '<' or i == '>' or i in output_tags:
        if '=' in i:
            output3.append(i.replace('=', ''))
        else:
            output3.append(i)

output4 = ' '.join(output3)

# split the string into list with elements only consisting of tags and/or attributes
output4 = re.findall(r"<[a-z0-9\s\=]+>", output4)

# generate final output - list of lists: each sublist consists of tag and/or attributes
output = []
for item in output4:
    output.append(re.findall(r"[a-z0-9]+", item))

# extra check for removal multi-tags from each sublist when they are not in [0] position:
output_tags = set(output_tags)
for i in output:
    if i[0] in output_tags:
        i[1:] = [j for j in i[1:] if j not in output_tags]

# join attributes to corresponding tag
temp1 = []
for i in output_tags:
    temp = [i]
    for j in output:
        if temp[0] == j[0]:
            if len(j) == 1:
                continue
            else:
                [temp.append(k) for k in j[1:] if k not in temp]
    temp1.append(temp)

# sort attributes of every tag if found:
for i in temp1:
    i[1:] = sorted(i[1:])

# sort the lists based on tag names:
temp1.sort(key=lambda i: i[0])

# print the output:
for i in temp1:
    print i[0] + ':' + ','.join(i[1:])
