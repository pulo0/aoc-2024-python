from utils.file_to_list_manager import get_file_to_list

lst = get_file_to_list('day4/input_day4.txt')

def part_one(grid):

    def is_valid(row, col, char):
        return 0 <= row < row_x and 0 <= col < col_y and grid[row][col] == char

    result = 0

    row_x, col_y = len(grid), len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    target_word = 'XMAS'
    target_letters = list(target_word)
    target_len = len(target_word)

    for x in range(row_x):
        for y in range(col_y):
            if grid[x][y] != target_letters[0]:
                continue
            for dir_x, dir_y in directions:
                if all(is_valid(x + dir_x * i, y + dir_y * i, target_letters[i]) for i in range(target_len)):
                    result += 1
    print(result)

def part_two(grid):

    row_x, col_y = len(grid), len(grid[0])

    result = 0

    for x in range(row_x - 2):
        for y in range(col_y - 2):
            pos_0 = grid[x][y] # Default position, top-left
            pos_1 = grid[x][y + 2] # position top-right
            pos_2 = grid[x + 1][y + 1] # middle position
            pos_3 = grid[x + 2][y] # position, bottom-left
            pos_4 = grid[x + 2][y + 2] # position, bottom-right
            if (pos_0 + pos_4 in {'MS', 'SM'}) and (pos_1 + pos_3 in {'MS', 'SM'}) and pos_2 == 'A':
                result += 1
    print(result)

choice = input('Select the answers of the forth Advent Of Code day: \n'
               + 'Part 1 (Press number 1) \n'
               + 'Part 2 (Press number 2) \n')

if choice == '1':
    part_one(lst)
elif choice == '2':
    part_two(lst)
else:
    print('Wrong choice')