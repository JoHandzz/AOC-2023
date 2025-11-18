def find_mirror_index(block: list[str]) -> int:
    potential_mirror = 0
    failed_mirror = 0
    
    start_line = block[0]
    
    while True:
        potential_mirror = 0 
        
        for mirror in range(1 + failed_mirror,len(start_line)):
            if all(l == r for l,r in zip(reversed(start_line[:mirror]),start_line[mirror:])):
                potential_mirror = mirror
                break
        
        if potential_mirror:
            is_valid_for_all = True 
            for line in block[1:]:
                if all(l == r for l,r in zip(reversed(line[:potential_mirror]),line[potential_mirror:])):
                    continue
                else:
                    failed_mirror = potential_mirror
                    is_valid_for_all = False
                    break 
            
            if is_valid_for_all:
                return potential_mirror
    
        if potential_mirror == 0:
            break
        

        if failed_mirror == len(start_line) - 1:
            break
            
    return 0


with open('13-data.txt','r') as f:
    all_text = f.read()
    blocks = [[line.strip() for line in block.split('\n') if line.strip()] 
              for block in all_text.split('\n\n') if block.strip()]
    

result = []
for block in blocks:
    vertical_mirror = find_mirror_index(block)
    if vertical_mirror:
        result.append(vertical_mirror)
        continue

    rotate_block = list(zip(*block))
    lateral_mirror = find_mirror_index(rotate_block)
    if lateral_mirror:
        result.append(lateral_mirror * 100)

print(sum(result))