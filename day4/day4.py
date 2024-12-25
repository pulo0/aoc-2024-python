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


part_one(lst)