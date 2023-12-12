with open("part_2/input.txt") as file:
    input = file.readlines()
input = [i.strip() for i in input]
input = [(i.split(' ')[0], int(i.split(' ')[1])) for i in input]

def rel_strength( str ):
    if str[0].isalpha():
        return {'A':13,'K':12,'Q':11,'T':10,'J':0}[str[0]]
    else:
        return int(str[0])

def joker( hand ):
    counts = { }
    for i in hand:
        if i != 'J': counts[i] = counts.get(i, 0)+1
    change_intos = [k for k, v in counts.items() if v==max(counts.values())]
    if change_intos:
        change_into = max(change_intos, key=lambda v: rel_strength(v))
    else:
        change_into = 'A'
    return hand.replace('J', change_into)

def type_of_hand( hand ):
    counts = { }
    hand = joker(hand)
    for i in hand: counts[i] = counts.get(i, 0)+1
    if 5 in counts.values():
        return 6
    elif 4 in counts.values():
        return 5
    elif 3 in counts.values():
        if 2 in counts.values():
            return 4
        return 3
    elif len( [i for i in counts.values() if i==2] ) == 2:
        return 2
    elif 2 in counts.values():
        return 1
    else:
        return 0

def compare( hand1, hand2 ):
    hinfo1 = (type_of_hand(hand1), [rel_strength(i) for i in hand1])
    hinfo2 = (type_of_hand(hand2), [rel_strength(i) for i in hand2])
    if hinfo1 < hinfo2:
        return -1
    if hinfo1 > hinfo2:
        return 1
    else:
        return 0

from functools import cmp_to_key

# print(joker("AJQ23"))

input.sort( key=cmp_to_key(lambda v1, v2: compare(v1[0], v2[0])) )
sum = 0
for i, v in enumerate(input):
    sum += (i+1)*v[1]
print(sum)