import sys
import re

regex_pattern1 = r"(?<=id\=\"question\-summary\-)[0-9]+"
regex_pattern2 = r"(?<=class\=\"question\-hyperlink\"\>)[A-Za-z0-9\s\,\)\(\?\-\+\]\[\.\&\#\;]+"
regex_pattern3 = r"(?<=class\=\"relativetime\"\>)[A-Za-z0-9\s\:]+"

regex_patterns1 = []
regex_patterns2 = []
regex_patterns3 = []
for line in sys.stdin:
    regex_patterns1.append(re.findall(regex_pattern1, line))
    regex_patterns2.append(re.findall(regex_pattern2, line))
    regex_patterns3.append(re.findall(regex_pattern3, line))

regex_patterns1 = [i for i in regex_patterns1 if i != []]
regex_patterns2 = [i for i in regex_patterns2 if i != []]
regex_patterns3 = [i for i in regex_patterns3 if i != []]

for i in range(len(regex_patterns1)):
    print ';'.join(regex_patterns1[i] + regex_patterns2[i] + regex_patterns3[i])    