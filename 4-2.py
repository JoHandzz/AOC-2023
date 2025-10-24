import re

test = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        """

# lines = test.strip().splitlines()


lines = []

with open('4-data.txt','r') as f:
    for string in f:
        lines.append(string.strip())



N_CHILDREN = {}

for line in lines:

    split_line = re.split(r'[:|]', line.strip())
    winning_nums = set(int(num) for num in split_line[1].strip().split(' ') if num.isdigit())
    my_nums = [int(num) for num in split_line[2].strip().split(' ') if num.isdigit()]
    card_ID = int(split_line[0].split()[-1]) 
    k = 0
    for num in my_nums:
        if num in winning_nums:
            k += 1

    N_CHILDREN[card_ID] = k


# print(CHILD_DIC)



FAMILY_SIZE = len(lines) 
number_of_copies = {ID: 1 for ID in N_CHILDREN.keys()} # Initialize all to have one (itself)


base_vertex = 1
while base_vertex <= FAMILY_SIZE:
    n_children = N_CHILDREN[base_vertex]
    for child in range(base_vertex + 1 , base_vertex + n_children + 1):
        number_of_copies[child] += number_of_copies[base_vertex]
    
    base_vertex += 1



print(sum(number_of_copies.values()))
            
