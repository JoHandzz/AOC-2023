test =  """
    ...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....

    """

# grid_lines = [line.strip() for line in test.splitlines() if line.strip()]

grid_lines = []
with open('11-data.txt','r') as f:
    for line in f:
        grid_lines.append(line.strip())



universe = {
    (x, y): val
    for y, line in enumerate(grid_lines) # y is the row index (0, 1, 2...)
    for x, val in enumerate(line)      # x is the column index (0, 1, 2...)
}

galaxy_index = 1

for key, val in universe.items():
    if val == '.':
        universe[key] = 0

    elif val == '#':
        universe[key] = galaxy_index
        galaxy_index += 1


n_cols = (max(x for x,_ in universe.keys())) + 1
n_rows = (max(y for _,y in universe.keys())) + 1



empty_rows = set()
for y in range(n_rows):
    is_empty = True
    for x in range(n_cols):
        if universe[x,y] > 0:
            is_empty = False
            break
    if is_empty:
        empty_rows.add(y)


empty_cols = set()
for x in range(n_cols):
    is_empty = True
    for y in range(n_rows):
        if universe[x,y] > 0:
            is_empty = False
            break
    if is_empty:
        empty_cols.add(x)


galaxy_map = {val: key for key, val in universe.items() if val > 0}


def distance(a,b):
    x1, y1 = galaxy_map[a]
    x2, y2 = galaxy_map[b]

    
    x_dis = abs(x2-x1)
    y_dis = abs(y2-y1)
    

    columns_in_path = set(x for x in range(min(x1, x2) + 1, max(x1, x2)))
    rows_in_path = set(y for y in range(min(y1, y2) + 1, max(y1, y2)))


    mult_val = 1000000 - 1 # set this to 1 for part 1 solution
    x_dis += len(empty_cols.intersection(columns_in_path)) * mult_val
    y_dis += len(empty_rows.intersection(rows_in_path)) * mult_val
 

    return x_dis + y_dis 



total_dis = 0
k = 0
for a in range(1,galaxy_index):
    for b in range(1 + k, galaxy_index):
        if a == b:
            continue

        total_dis += distance(a,b)
    k += 1

print(total_dis)



    
##### GOD IDE FRA GEMINI 
# nemmere måde at finde tomme rows and columns


# --- Alternative way to find empty rows/cols ---

# # 1. Find all galaxy coordinates first
# galaxy_coords = set()
# for (x, y), val in universe.items():
#     if val == '#':
#         galaxy_coords.add((x, y))

# # 2. Get all x's and y's that have galaxies
# occupied_rows = {y for _, y in galaxy_coords}
# occupied_cols = {x for x, _ in galaxy_coords}

# # 3. Find the ones that are empty
# all_rows = set(range(n_rows))
# all_cols = set(range(n_cols))

# empty_rows = all_rows - occupied_rows  # Set difference!
# empty_cols = all_cols - occupied_cols