lst = [('0', 'zero') ,
       ('1', 'one') ,
       ('2', 'two') ,
       ('3', 'three') ,
       ('4', 'four') ,
       ('5', 'five') ,
       ('6', 'six') ,
       ('7', 'seven') ,
       ('8', 'eight') ,
       ('9', 'nine')]




def main(txt):
    def check_for_match(substring, word_list):
        for num, word in word_list:
            if word in substring:
                return num, word 
        return None, None
    
    def is_num(a):
        return ord('0') <= ord(a) <= ord('9')

    
    l = 0
    while l < len(txt):
         
        txt_from_left = txt[:l]
        num, word = check_for_match(txt_from_left, lst)
        
        if word:
            left_digit = num
            break

        elif is_num(txt[l]):
             left_digit = txt[l]
             break

        l += 1 
         
        

    r = len(txt) - 1 
    while r >= 0:
                
        txt_from_right = txt[r:]
        num, word = check_for_match(txt_from_right, lst)
        
        if word:
            right_digit = num
            break

    
        elif is_num(txt[r]):
             right_digit = txt[r]
             break
        
        r -= 1 
         
    return int(left_digit + right_digit)
            


cur_sum = 0

with open('1-data.txt', 'r') as f:
    for line in f:
        cur_sum += main(line)


print(cur_sum)

