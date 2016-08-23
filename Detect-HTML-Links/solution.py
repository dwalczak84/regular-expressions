import re

regex_pattern = r'<a href="(.*?)".*?>([\w ,./]*)(?=</)'

N = int(raw_input())
for _ in range(N):
    line = raw_input()
    output = re.findall(regex_pattern, line)
    for link, title in output:
        print "{},{}".format(link, title.strip())