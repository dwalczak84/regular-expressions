N = int(raw_input())
test_strings = []
for i in range(N):
    S = raw_input()
    test_strings.append(S)

regex_pattern_IPv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
regex_pattern_IPv6 = r'^([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$'

for string in test_strings:
    if bool(re.search(regex_pattern_IPv4, string)):
        print 'IPv4'
    elif bool(re.search(regex_pattern_IPv6, string)):
        print 'IPv6'
    else:
        print 'Neither'