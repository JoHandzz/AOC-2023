types_of_hands = ['fiveofkind', 'fourofkind', 'fullhouse', 'threeofkind', 'twopair', 'onepair', 'highcard']

hands_dic = {}

with open('7-data.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split(" ")
        hands_dic[key] = int(value)



hands_by_type = {type_hand : [] for type_hand in types_of_hands}

for hand in hands_dic.keys():
    cur_hand_counts = {}
    for char in hand:
        cur_hand_counts[char] = cur_hand_counts.get(char, 0) + 1
    
    joker_count = cur_hand_counts.pop('J', 0)

    counts = sorted(cur_hand_counts.values(), reverse=True)
    
    if not counts:
        counts = [0] 
        
    counts[0] += joker_count
    
    if counts == [5]:
        hands_by_type['fiveofkind'].append(hand)
    elif counts == [4, 1]:
        hands_by_type['fourofkind'].append(hand)
    elif counts == [3, 2]:
        hands_by_type['fullhouse'].append(hand)
    elif counts == [3, 1, 1]:
        hands_by_type['threeofkind'].append(hand)
    elif counts == [2, 2, 1]:
        hands_by_type['twopair'].append(hand)
    elif counts == [2, 1, 1, 1]:
        hands_by_type['onepair'].append(hand)
    else:
        hands_by_type['highcard'].append(hand)

    
final_list = []
types_of_hands.reverse() 


strength_map = {
    'A': 'm', 'K': 'l', 'Q': 'k', 'T': 'j',
    '9': 'i', '8': 'h', '7': 'g', '6': 'f', '5': 'e',
    '4': 'd', '3': 'c', '2': 'b', 'J': 'a'
}

for type_hand in types_of_hands: 
    hands_in_type = hands_by_type[type_hand]
    
    # Sort hands of the same type using the strength_map
    # A lambda function translates each hand (e.g., "T55J5") 
    # into a new string (e.g., "idjjd") which can be sorted alphabetically.
    sorted_hands = sorted(
        hands_in_type, 
        key=lambda hand: "".join(strength_map[card] for card in hand)
    )
    
    final_list = final_list + sorted_hands


final_sum = 0
for rank, hand in enumerate(final_list):
    final_sum += (hands_dic[hand] * (rank + 1))

print(final_sum) 



