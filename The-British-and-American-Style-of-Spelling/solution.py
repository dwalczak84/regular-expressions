def uk_and_us_style_of_spelling(lines, test_cases):

    import re
    import string
    regex_pattern = r"(\w+ze\w+|\w+se\w+|\w+ze|\w+se)"
    words_found = []
    for line in lines:
        words_found.extend(re.findall(regex_pattern, line))
    fi
    results = []
    for word in test_cases:
        results.append(words_found.count(string.replace(word, 'ze', 'se')) + words_found.count(word))
        
    for result in results:
        print result

N = int(raw_input())
lines = []
for i in xrange(N):
    line = raw_input()
    lines.append(line)

T = int(raw_input())
test_cases = []
for i in xrange(T):
    test_word = raw_input()
    test_cases.append(test_word)

uk_and_us_style_of_spelling(lines, test_cases)
