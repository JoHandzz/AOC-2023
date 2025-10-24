
import re

score = 0

with open('4-data.txt', 'r') as f:
    for line in f:
        split_line = re.split(r'[:|]', line.strip())
        winning_nums = set(int(num) for num in split_line[1].strip().split(' ') if num.isdigit())
        my_nums = [int(num) for num in split_line[2].strip().split(' ') if num.isdigit()]

        k = 0
        for num in my_nums:
            if num in winning_nums:
                k += 1
        
        

        score += 2**(k-1) if (k > 0) else 0

print(score)
        



        
        
