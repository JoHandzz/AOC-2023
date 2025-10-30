"""
TEST INPUT
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483


hands_dic = {'32T3K': 765,
              'T55J5': 684,
              'KK677': 28,
              'KTHHT': 220,
              'QQQJA': 483
              }

"""

types_of_hands = ['fiveofkind', 'fourofkind', 'fullhouse', 'threeofkind', 'twopair', 'onepair', 'highcard']

hands_dic = {}

with open('7-data.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split(" ")
        hands_dic[key] = int(value)



def is_5ofkind(hand_dic):
    return (5 in hand_dic.values())


def is_4ofkind(hand_dic):
    return (4 in hand_dic.values())


def is_fullhouse(hand_dic):
    return (3 in hand_dic.values() and 2 in hand_dic.values())


def is_3ofkind(hand_dic):
    return 3 in hand_dic.values()

def is_2pair(hand_dic):
    return len([x for x in hand_dic.values() if x == 2]) == 2

def is_1pair(hand_dic):
    return len(hand_dic.values()) == 4 and 2 in hand_dic.values()


hands_by_type = {type_hand : [] for type_hand in types_of_hands}


print(hands_by_type)


for hand in hands_dic.keys():
    cur_hand = {}
    for char in hand:
        if char in cur_hand:
            cur_hand[char] += 1
        else:
            cur_hand[char] = 1
    
    if is_5ofkind(cur_hand):
        hands_by_type['fiveofkind'].append(hand)
    
    elif is_4ofkind(cur_hand):
        hands_by_type['fourofkind'].append(hand)
    
    elif is_fullhouse(cur_hand):
        hands_by_type['fullhouse'].append(hand)
    
    elif is_3ofkind(cur_hand):
        hands_by_type['threeofkind'].append(hand)
    

    elif is_2pair(cur_hand):
        hands_by_type['twopair'].append(hand)
    

    elif is_1pair(cur_hand):
        hands_by_type['onepair'].append(hand)
    
    else:
        hands_by_type['highcard'].append(hand)
    
final_list = []
types_of_hands.reverse() 

# 2. CREATE a map to translate card values for correct sorting
strength_map = {
    'A': 'm', 'K': 'l', 'Q': 'k', 'J': 'j', 'T': 'i',
    '9': 'h', '8': 'g', '7': 'f', '6': 'e', '5': 'd',
    '4': 'c', '3': 'b', '2': 'a'
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
    # this is called: The "Decorate-Sort-Undecorate" Pattern
    
    final_list = final_list + sorted_hands


final_sum = 0
for rank, hand in enumerate(final_list):
    final_sum += (hands_dic[hand] * (rank + 1))

print(final_sum) 