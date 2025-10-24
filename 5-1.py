lines = []


with open('5-data.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())


seeds = [int(num) for num in lines[0].split(':')[1].split(' ') if num.strip()]
lines_after_seeds = lines[1:]

conversions = {}
current_map_name = None
current_map_ranges = []

for line in lines_after_seeds:
    if line.endswith('map:'):
        if current_map_name:
            conversions[current_map_name] = current_map_ranges
        
     
        current_map_name = line.split(' ')[0]  
        current_map_ranges = []  
    
    elif line.strip() == "":
        pass
        
    elif current_map_name:
        
        nums = [int(num) for num in line.split(' ') if num.strip()]
        
        if len(nums) == 3:
            dest_start, source_start, range_len = nums
            current_map_ranges.append((dest_start, source_start, range_len))
    

if current_map_name:
    conversions[current_map_name] = current_map_ranges




def mapping(values_lst,val):
    for i in values_lst:
        des, source, lenght = i
        if source <= val < source + lenght:
            diff = des - source
            return (val + diff)
    return val

min_seed = 1000000000000
for seed in seeds:
    for conversion_type in conversions.keys():
        seed = mapping(conversions[conversion_type],seed)
    
    min_seed = min(min_seed,seed)

print(min_seed)
    






    

        
    