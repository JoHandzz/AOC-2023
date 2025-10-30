test =   """
    0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45
    """

l = [[int(num) for num in line.strip().split(' ')] for line in test.splitlines() if line.strip()]



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
    
    all_sublists = list(reversed(all_sublists))
    print(all_sublists)
    

    val = 0
    for lst in all_sublists:
        prev_num = lst[0] - val
        print(prev_num)
        lst = [prev_num] + lst
        print(lst)
        val = lst[0]
        print(val)
        
    return val


print(previous_num(l[2]))