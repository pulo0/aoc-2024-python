# Advent of Code 2024, Day 1
# Source: https://adventofcode.com/2024/day/1
# Date: 2024-12-01
with open('input_day.txt') as file:
    listInitial = []
    listFirst = []
    listSecond = []
    for i in file.readlines():
        eachItem = i.split()
        listInitial.append(eachItem)
    for j in range(0, len(listInitial)):
        listFirst.append(listInitial[j][0])
        listSecond.append(listInitial[j][1])
    sListFirst = sorted(listFirst)
    sListSecond = sorted(listSecond)


def firstPart():
    result = 0
    for k in range(0, len(listInitial)):
        divisionForFirst = int(sListFirst[k]) - int(sListSecond[k])
        divisionForSecond = int(sListSecond[k]) - int(sListFirst[k])
        if sListFirst[k] > sListSecond[k]:
            result += divisionForFirst
        else:
            result += divisionForSecond
    print(result)


def secondPart():
    result = 0
    for k in range(0, len(listInitial)):
        multiply = 0
        for l in range(0, len(listInitial)):
            if sListFirst[k] == sListSecond[l]:
                multiply += 1
        result += int(sListFirst[k]) * multiply
    print(result)


choice = input('Select the answers of the first Advent Of Code day: \n'
               + 'Part 1 (Press number 1) \n'
               + 'Part 2 (Press number 2) \n')

if choice == '1':
    firstPart()
elif choice == '2':
    secondPart()
else:
    print('Wrong choice')
