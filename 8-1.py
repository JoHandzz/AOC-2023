"""
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

instruction = "LLR"

network = {
    'AAA': ('BBB', 'BBB'),
    'BBB': ('AAA', 'ZZZ'),
    'ZZZ': ('ZZZ', 'ZZZ')
}

"""
lines = []
with open('8-data.txt','r') as f:
    for line in f:
        lines.append(line.strip())


instruction = lines[0]

network = {}
for item in lines[2:]:
    key, string_val = item.split('=')
    left,right = string_val.replace('(','').replace(')','').split(',')
    network[key.strip()] = (left.strip(), right.strip())



note = 'AAA'
steps = 0

while note != 'ZZZ':
    for direction in instruction:
        steps += 1
        left_note, right_note = network[note]

        if direction == 'L':
            note = left_note
            
        elif direction == 'R':
            note = right_note

    
print(steps)
    

            
    

