test =   """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """

test_lines = [[int(num) for num in line.strip().split(' ')] for line in test.splitlines() if line.strip()]
l1 = test_lines[0]



def next_num(lst):
    def sublist(lst):
        sublist = []
        pointer = 0
        while pointer < len(lst) - 1:
                sublist.append(lst[pointer + 1] - lst[pointer])
                pointer += 1
            
        return sublist
    
    all_sublists = [lst]
    while any(x for x in lst):
        lst = sublist(lst)
        all_sublists.append(lst)

    val = 0
    for lst in reversed(all_sublists):
        lst.append(val + lst[-1])
        val = lst[-1]
        
    return val



def previous_num(lst):
    def sublist(lst):
        sublist = []
        pointer = 0
        while pointer < len(lst) - 1:
                sublist.append(lst[pointer + 1] - lst[pointer])
                pointer += 1
            
        return sublist
    
    all_sublists = [lst]
    while any(x for x in lst):
        lst = sublist(lst)
        all_sublists.append(lst)
    
    # all_sublists = list(reversed(all_sublists))
    all_sublists = all_sublists[::-1]

    val = 0
    for lst in all_sublists:
        prev_num = lst[0] - val
        lst = [prev_num] + lst
        val = lst[0]
        
    return val


lines = []
with open('9-data.txt','r') as f:
     for line in f:
          lines.append([int(num) for num in line.strip().split(' ')])


final_number = 0
for line in lines:
     final_number += previous_num(line)

print(final_number)
     


