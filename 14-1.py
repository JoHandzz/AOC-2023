import numpy as np

def sort_column(column):
    made_a_change = True
    while made_a_change:
        made_a_change = False
        for i in range(1, len(column)):
            if column[i] == 'O' and column[i - 1] == '.':
                column[i], column[i - 1] = column[i - 1], column[i]
                made_a_change = True
    return column




with open('14-data.txt', 'r') as f:
    grid = np.array([[tile for tile in line.strip()] for line in f if line.strip()])


for column in range(len(grid[0])):
    grid[:,column] = sort_column(grid[:,column])


points = 0
val = len(grid)

for row in range(len(grid)):
    for i in grid[row]:
        if i == 'O':
            points += val
    val -= 1

print(points)