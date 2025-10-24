test = """
    Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    """

test_lines = [line.strip() for line in test.splitlines() if line.strip()]


max_sample = {'red': 12,
              'green': 13,
              'blue': 14}

def main(txt_line):

    ID, data = txt_line.split(':')
    ID_num = ID.split(' ')[-1]
    samples = [sample for sample in data.split(';')]
    dic = {}

    for sample in samples:
        lst = [item for item in sample.split(',')]
        for i in lst:
            num, color = i.strip().split(' ')
            dic[color] = int(num)
        
        for color in dic.keys():
            if dic[color] > max_sample[color]:
                return 0
        
        dic.clear()
    
    return int(ID_num)
        

my_sum = 0
with open('2-data.txt', 'r') as f:
    for line in f:
        my_sum += main(line)


print(my_sum)
        
        


####### IDIOMATIC SOLUTION #########


MAX_CUBES = {'red': 12, 'green': 13, 'blue': 14}

def get_valid_game_id_pythonic(line):
    """Checks if a game is valid using a generator and all()."""
    
    try:
        game_prefix, all_samples_str = line.split(':')
        game_id = int(game_prefix.split(' ')[-1])

        # This is a nested generator expression.
        # It yields (num_str, color) tuples for every single pull in the game
        # without building big lists in memory.
        all_pulls = (
            pull.strip().split(' ')
            for sample_str in all_samples_str.split(';')
            for pull in sample_str.split(',')
        )


        # all() checks if every item in the generator is True.
        # It stops and returns False as soon as it finds one invalid pull.
        is_valid = all(
            int(num_str) <= MAX_CUBES.get(color, 0)
            for num_str, color in all_pulls
        )

        return game_id if is_valid else 0
    
    except (ValueError, AttributeError):
        return 0

# --- Main logic ---
my_sum = 0
try:
    with open('2-data.txt', 'r') as f:
        my_sum = sum(get_valid_game_id_pythonic(line.strip()) for line in f)
    print(my_sum)
except FileNotFoundError:
    print("Error: '2-data.txt' file not found.")
