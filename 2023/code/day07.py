import os
import re
import numpy as np

day = 7

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

def hand_to_kind(hand):

    assert(len(hand)==5)
    sorted_hand = sorted(hand)
    matches = [0] * 5

    j = 0
    a = sorted_hand[0]
    for c in sorted_hand:
        if c == a:
            matches[j] += 1
        else:
            a = c
            j += 1
            matches[j] = 1

    matches = sorted(matches,reverse=True)

    if   matches == [5,0,0,0,0]:
        return "five_kind"
    elif matches == [4,1,0,0,0]:
        return "four_kind"
    elif matches == [3,2,0,0,0]:
        return "full_house"
    elif matches == [3,1,1,0,0]:
        return "three_kind"
    elif matches == [2,2,1,0,0]:
        return "two_pair"
    elif matches == [2,1,1,1,0]:
        return "one_pair"
    elif matches == [1,1,1,1,1]:
        return "high_card"
    else:
        raise ValueError(f"Something wrong with sorted matches: {matches}")

def hand_to_points(hand):

    assert(len(hand)==5)

    kind = hand_to_kind(hand)

    a = kind_to_int[kind]
    b = 0
    for i in hand:
        b = 100 * b + label_to_int[i]

    return b + 100000000000 * a

with open(true_input,'r') as f:

    kind_to_int = { "five_kind": 6,
                    "four_kind": 5,
                    "full_house": 4,
                    "three_kind": 3,
                    "two_pair": 2,
                    "one_pair": 1,
                    "high_card": 0}

    label_to_int = {"A": 14, "K": 13, "Q": 12, "J": 11,
                    "T": 10, "9": 9, "8": 8, "7": 7,
                    "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

    all_hands = []
    all_bids  = {}
    for l in f:
        a = re.split(r'\s+',l)
        all_hands.append(a[0])
        all_bids[a[0]] = [ int(a[1]), 0]

    all_hands = sorted(all_hands,key=hand_to_points)
    for i,h in enumerate(all_hands,start=1):
        all_bids[h][1] = i

    for key, val in all_bids.items():
        ans += val[0] * val[1]

print(f"part 1 = {ans}")


## part 2

ans = 0

def hand_to_kind(hand):

    assert(len(hand)==5)
    sorted_hand = sorted(hand)
    matches = [0] * 5

    j = 0
    a = sorted_hand[0]
    for c in sorted_hand:
        if c == a:
            matches[j] += 1
        else:
            a = c
            j += 1
            matches[j] = 1

    matches = sorted(matches,reverse=True)

    num_jokers = sum([1 if c == "J" else 0 for c in hand ])

    # if five_kind, jokers don't matter
    if   matches == [5,0,0,0,0]:
        return "five_kind"
    elif matches == [4,1,0,0,0] and num_jokers == 0:
        return "four_kind"
    elif matches == [4,1,0,0,0] and (num_jokers == 1 or num_jokers == 4):
        return "five_kind"
    elif matches == [3,2,0,0,0] and num_jokers == 0:
        return "full_house"
    elif matches == [3,2,0,0,0] and (num_jokers == 3 or num_jokers == 2):
        return "five_kind"
    elif matches == [3,1,1,0,0] and num_jokers == 0:
        return "three_kind"
    elif matches == [3,1,1,0,0] and (num_jokers == 1 or num_jokers == 3):
        return "four_kind"
    elif matches == [2,2,1,0,0] and num_jokers == 0:
        return "two_pair"
    elif matches == [2,2,1,0,0] and num_jokers == 2:
        return "four_kind"
    elif matches == [2,2,1,0,0] and num_jokers == 1:
        return "full_house"
    elif matches == [2,1,1,1,0] and num_jokers == 0:
        return "one_pair"
    elif matches == [2,1,1,1,0] and (num_jokers == 2 or num_jokers == 1):
        return "three_kind"
    elif matches == [1,1,1,1,1] and num_jokers == 0:
        return "high_card"
    elif matches == [1,1,1,1,1] and num_jokers == 1:
        return "one_pair"
    else:
        raise ValueError(f"Something wrong with sorted matches: {matches}")

def hand_to_points(hand):

    assert(len(hand)==5)

    kind = hand_to_kind(hand)

    a = kind_to_int[kind]
    b = 0
    for i in hand:
        b = 100 * b + label_to_int[i]

    return b + 100000000000 * a

with open(true_input,'r') as f:

    kind_to_int = { "five_kind": 6,
                    "four_kind": 5,
                    "full_house": 4,
                    "three_kind": 3,
                    "two_pair": 2,
                    "one_pair": 1,
                    "high_card": 0}

    label_to_int = {"A": 14, "K": 13, "Q": 12,
                    "T": 10, "9": 9, "8": 8, "7": 7,
                    "6": 6, "5": 5, "4": 4, "3": 3,
                    "2": 2, "J": 1}

    all_hands = []
    all_bids  = {}
    for l in f:
        a = re.split(r'\s+',l)
        all_hands.append(a[0])
        all_bids[a[0]] = [ int(a[1]), 0]

    all_hands = sorted(all_hands,key=hand_to_points)
    for i,h in enumerate(all_hands,start=1):
        all_bids[h][1] = i

    for key, val in all_bids.items():
        ans += val[0] * val[1]

print(f"part 2 = {ans}")
