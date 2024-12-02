# Task: Advent of Code 2024, Day 2
# Source of the task: https://adventofcode.com/2024/day/2
# Date: 2024-12-02
with open('input_day2.txt') as file:
    list_initial = []
    for line in file.readlines():
        each_item = list(map(int, line.split()))
        list_initial.append(each_item)


def part_one():
    result = 0
    for j in range(len(list_initial)):
        asc_checker = 0
        desc_checker = 0
        for k in range(len(list_initial[j]) - 1):
            amount = 0
            lst = list_initial[j]
            asc = lst[k+1] - lst[k]
            desc = lst[k] - lst[k+1]
            if asc > 0 and desc_checker == 0:
                match asc:
                    case 1 | 2 | 3:
                        asc_checker += 1
                        amount += 1
                    case _:
                        amount = 0
                        break
            elif desc > 0 and asc_checker == 0:
                match desc:
                    case 1 | 2 | 3:
                        desc_checker += 1
                        amount += 1
                    case _:
                        amount = 0
                        break
            else:
                amount = 0
                break
        if amount > 0:
            result += 1
    print(result)


def is_safe(report):
    diffr = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    asc = all(1 <= diff <= 3 for diff in diffr)
    desc = all(-3 <= diff <= -1 for diff in diffr)
    return asc or desc


def is_safe_one_remove(report):
    for i in range(len(report)):
        mod_report = report[:i] + report[i+1:]
        if is_safe(mod_report):
            return True
    return False


def part_two():
    result = 0
    for report in list_initial:
        if is_safe(report) or is_safe_one_remove(report):
            result += 1

    print(result)


choice = input('Select the answers of the first Advent Of Code day: \n'
               + 'Part 1 (Press number 1) \n'
               + 'Part 2 (Press number 2) \n')

if choice == '1':
    part_one()
elif choice == '2':
    part_two()
else:
    print('Wrong choice')
