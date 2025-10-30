
grid_lines = []
with open('10-dataX.txt','r') as f:
    for line in f:
        grid_lines.append(line.strip())


grid_dic = {
    (x, y): val
    for y, line in enumerate(grid_lines) # y is the row index (0, 1, 2...)
    for x, val in enumerate(line)      # x is the column index (0, 1, 2...)
}


start_tile = ((108, 36), 'below') # Manualy found and replaced in the 10-data.txt


above = {
    '|': ((0,1), 'above'),
    'J': ((-1,0), 'right'),
    'L': ((1,0), 'left')
}

below = {
    '|': ((0,-1), 'below'),
    '7': ((-1,0), 'right'),
    'F': ((1,0), 'left')
}

left = {
    '-': ((1,0), 'left'),
    'J': ((0,-1), 'below'),
    '7': ((0,1), 'above'),
}

right = {
    '-': ((-1,0), 'right'),
    'L': ((0,-1), 'below'),
    'F': ((0,1), 'above')
}

direction_dir = {
    'above': above,
    'below': below,
    'right': right,
    'left': left
}



def get_new_tile(cur_tile):
    (x, y) , direction = cur_tile
    char = grid_dic[(x,y)]
    (dx, dy), new_direction = direction_dir[direction][char]

    return ((dx + x, dy + y), new_direction)


tile = start_tile
tiles_gone_through = 0


while True:
    tile = get_new_tile(tile)
    print(tile)
    tiles_gone_through += 1
    if tile == start_tile:
        break

print(tiles_gone_through/2)
