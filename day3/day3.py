# Advent of Code 2024, Day 3
# Source: https://adventofcode.com/2024/day/3
# Date: 2024-12-03

import re

pattern = re.compile(r"(?:mul\((\d{1,})\,(\d{1,})\))")
pattern_part_two = re.compile(
    r"(?:mul\((\d{1,})\,(\d{1,})\))|(?:(don\'t\(\)))|(?:(do\(\)))")


# First part
def part_one():

    list_initial = []
    for i, line in enumerate(open('input_day3.txt')):
        for match in re.finditer(pattern, line):
            list_initial.append(match.group(1))
            list_initial.append(match.group(2))

    result = 0
    for j in range(0, len(list_initial) - 1, 2):
        result += int(list_initial[j]) * int(list_initial[j+1])
    print(result)


# Second part
list_initial = []
def prepare():
    for i, line in enumerate(open('input_day3.txt')):
        for match in re.finditer(pattern_part_two, line):
            list_initial.append(match.group())


def transform_mul(lst):
    srt = re.findall(r'\b\d+\b', lst)
    return int(srt[0]) * int(srt[1])


def part_two():
    prepare()

    result = 0
    is_Dont = False
    for j in range(len(list_initial) - 1):
        if list_initial[j] == "don't()":
            is_Dont = True
        elif list_initial[j] == "do()":
            is_Dont = False
        else:
            if is_Dont == False:
                both = transform_mul(list_initial[j])
                result += both
    print(result)


choice = input('Select the answers of the third Advent Of Code day: \n'
               + 'Part 1 (Press number 1) \n'
               + 'Part 2 (Press number 2) \n')

if choice == '1':
    part_one()
elif choice == '2':
    part_two()
else:
    print('Wrong choice')
