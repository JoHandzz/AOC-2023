"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

"""



grid = []

with open('16-data.txt', 'r') as f:
    for line in f:
        grid.append((line.strip()))




# A (row, column) coordinates (dy, dx).
RIGHT = (0, 1)
LEFT  = (0, -1)
UP    = (-1, 0)
DOWN  = (1, 0)


TRANSITION_RULES = {
    '.': {
        RIGHT: [RIGHT],
        LEFT:  [LEFT],
        UP:    [UP],
        DOWN:  [DOWN]
    },


    '/': {
        RIGHT: [UP],
        LEFT:  [DOWN],
        UP:    [RIGHT],
        DOWN:  [LEFT]
    },

    '\\': {
        RIGHT: [DOWN],
        LEFT:  [UP],
        UP:    [LEFT],
        DOWN:  [RIGHT]
    },

    '|': {
        UP:    [UP],
        DOWN:  [DOWN],
        RIGHT: [UP, DOWN],  
        LEFT:  [UP, DOWN]   
    },

    '-': {
        LEFT:  [LEFT],
        RIGHT: [RIGHT],
        UP:    [LEFT, RIGHT], # Splits!
        DOWN:  [LEFT, RIGHT]  # Splits!
    }
}

