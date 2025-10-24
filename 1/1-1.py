txt1 = "1abc2"
txt3 = "treb7uchet"


def is_num(a):
    return ord('0') <= ord(a) <= ord('9')

def main(txt):
    l, r = 0, len(txt) - 1
    first_num = ""
    second_num = ""

    while not first_num:
        if is_num(txt[l]):
            first_num = txt[l]
            # break, does it need brake statement here?
        else:
            l += 1
    
    while not second_num:
        if is_num(txt[r]):
            second_num = txt[r]
            
        else:
            r -= 1
    
    return int(first_num + second_num)


cur_sum = 0

with open('1-data.txt', 'r') as f:
    for line in f:
        cur_sum += main(line)
        

print(cur_sum)


###### IDIOMATIC SOLUTION 

def main_idiomatic(txt):
    # 1. Filter the string to get a list of all digit characters
    digits = [char for char in txt if char.isdigit()]
    
    # 2. Check if any digits were found (good practice for safety)
    if not digits:
        return 0 # Or raise an error, depending on requirements

    # 3. Concatenate the first and last digit, then convert to integer
    return int(digits[0] + digits[-1])

# --- Usage Example ---
cur_sum_idiomatic = 0

with open('1-data.txt', 'r') as f:
    for line in f:
        # The .strip() is important to remove the newline character
        # which can sometimes cause issues or is just good practice
        cur_sum_idiomatic += main_idiomatic(line.strip())
        