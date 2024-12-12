def get_file_to_list(file: str):
    choice = int(input(
        '''
            How do you want to format the input of the file:
            1. Each letter in a line as an item to a list (Press 1)
            2. Each number in a line as an item to a list (Press 2) 
        '''))

    if choice == 1:
        with open(file) as f:
            list_initial = []
            for line in f.readlines():
                each_item = list(map(int, line.split()))
                list_initial.append(each_item)
        return list_initial
    elif choice == 2:
        with open(file, 'r') as f:
            lst = [list(item.strip()) for item in f.readlines()]
        return lst
    else:
        print('You entered wrong option')
        return 0
