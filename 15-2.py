def get_hash(string):
    val = 0
    for char in string:
        val += ord(char)
        val *= 17
        val %=  256
    return val


def main(lst):
    parced_data = []
    boxes = {i : [] for i in range(256)}


    for string in lst:
        if '=' in string:
            operator = '='
            label, focal_len = string.split('=')

        else:
            operator = '-'
            label = string.split('-')[0]
            focal_len = None
        
        parced_data.append((get_hash(label), label, operator, focal_len))



    for hash_val, label, operator, focal_len in parced_data:
        box_content = boxes[hash_val]
        used_labels = [label for label, _ in box_content]

        if operator == '=':

            if label in used_labels:
                replace_idx = used_labels.index(label)
                box_content[replace_idx] = ((label, focal_len))

            else:
                box_content.append((label, focal_len))
        
        else:
            if label in used_labels:
                replace_idx = used_labels.index(label)
                del box_content[replace_idx]



    total_sum = 0       
    for box_n, lst in boxes.items():
        val = 0
        if lst:
            for i, lens in enumerate(lst):
                val += (box_n + 1) * (i + 1) * int(lens[1])
            
            total_sum += val
    
    return total_sum



if __name__ == "__main__":

    with open('15-data.txt', 'r') as f:
        data = f.read()
        lst = [string.strip() for string in data.split(',')]
    
    print(main(lst))







    














