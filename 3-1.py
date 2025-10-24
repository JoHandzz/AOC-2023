import re

TEST_MAP =   [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

MAP = []

with open('3-data.txt','r') as f:
    for line in f:
        MAP.append(line.strip())


W = len(MAP[0])
H = len(MAP)



def find_nums(my_str):
    lst = []
    # Use re.finditer to get match objects with start/span information
    for match in re.finditer(r'\d+', my_str):
        # match.group(0) is the number string, match.start() is its correct index
        lst.append((match.group(0), match.start()))

    return lst



def index_to_check(y, start_x, num_len): 
    surrounding = []
    
    for row_y in range(y - 1, y + 2):
        for col_x in range(start_x - 1, start_x + num_len + 1):
            
            is_part_of_number = (row_y == y and start_x <= col_x < start_x + num_len)
            if is_part_of_number:
                continue
            
            is_y_valid = 0 <= row_y < H
            is_x_valid = 0 <= col_x < W

            if is_y_valid and is_x_valid:
                surrounding.append((row_y, col_x))

    return surrounding


def is_char(y,x):
    tile = MAP[y][x]
    return not (tile == "." or tile.isdigit())




def main():
    my_sum = 0
    for y, row in enumerate(MAP):
        for num, x in find_nums(row):
            indexes = index_to_check(y, x, len(num))
            if any(is_char(y,x) for y,x in indexes):
                my_sum += int(num)
    
    print(my_sum)





main()
