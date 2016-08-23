import re

def count_occurrences(lines, substrings):

    for substring in substrings:
        pattern = get_pattern(substring)
        count = sum(len(pattern.findall(line)) for line in lines)
        print(count)

def get_pattern(substring):

    regex = '\w{0}\w'.format(substring)
    pattern = re.compile(regex)
    return pattern

if __name__ == '__main__':

    line_count = int(input())
    lines = [input() for _ in range(line_count)]
    substring_count = int(input()
    substrings = (input() for _ in range(substring_count))
    count_occurrences(lines, substrings)

