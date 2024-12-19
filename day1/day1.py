# Advent of Code 2024, Day 1
# Source: https://adventofcode.com/2024/day/1
# Date: 2024-12-01
with open('input_day.txt') as file:
    list_initial = []
    list_first = []
    list_second = []
    for i in file.readlines():
        eachItem = i.split()
        list_initial.append(eachItem)
    for j in range(0, len(list_initial)):
        list_first.append(list_initial[j][0])
        list_second.append(list_initial[j][1])
    s_list_first = sorted(list_first)
    s_list_second = sorted(list_second)


def first_part():
    result = 0
    for k in range(0, len(list_initial)):
        division_for_first = int(s_list_first[k]) - int(s_list_second[k])
        division_for_second = int(s_list_second[k]) - int(s_list_first[k])
        if s_list_first[k] > s_list_second[k]:
            result += division_for_first
        else:
            result += division_for_second
    print(result)


def second_part():
    result = 0
    for k in range(0, len(list_initial)):
        multiply = 0
        for l in range(0, len(list_initial)):
            if s_list_first[k] == s_list_second[l]:
                multiply += 1
        result += int(s_list_first[k]) * multiply
    print(result)


choice = input('Select the answers of the first Advent Of Code day: \n'
               + 'Part 1 (Press number 1) \n'
               + 'Part 2 (Press number 2) \n')

if choice == '1':
    first_part()
elif choice == '2':
    second_part()
else:
    print('Wrong choice')
