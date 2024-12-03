# Advent of Code 2024, Day 3
# Source: https://adventofcode.com/2024/day/3
# Date: 2024-12-03

import re

pattern = re.compile(r"(?:mul\((\d{1,})\,(\d{1,})\))")

list_initial = []
for i, line in enumerate(open('input_day3.txt')):
    for match in re.finditer(pattern, line):
        list_initial.append(match.group(1))
        list_initial.append(match.group(2))
        
def part_one():
    result = 0
    for j in range(0, len(list_initial) - 1, 2):
        result += int(list_initial[j]) * int(list_initial[j+1])
    print(result)