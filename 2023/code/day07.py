import os
import re

day = 7

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

def is_five_kind(hand):

    assert(len(hand)==5)

    out = True

    for c in hand:
        for d in hand:
            out = out and c == d

    return out

def is_four_kind(hand):

    assert( len(hand) == 5 )

    return out

def is_high_card(hand):

    assert(len(hand)==5)

    out = True

    for i,c in hand:
        for d in hand[i+1:]:
            out = out and c != d

    return out

def matchings(hand):

    assert(len(hand)==5)
    matchs = [0] * 5
    for i,c in enumerate(hand):
        for d in hand[i+1]:
            if c == d:
                matchs[i] += 1

    # sort
    sorted_matchs = sorted(matchs)

    if   sorted_matchs == [5,0,0,0,0]:
        return "five_kind"
    elif sorted_matchs == [4,1,0,0,0]:
        return "four_kind"
    elif sorted_matchs == [3,1,1,0,0]:
        return "three_kind"
    elif sorted_matchs == [3,2,0,0,0]:
        return "full_house"
    elif sorted_matchs == [2,2,1,0,0]:
        return "two_pair"
    elif sorted_matchs == [2,1,1,1,0]:
        return "one_pair"
    elif sorted_matchs == [1,1,1,1,1]:
        return "high_card"
    else:
        raise ValueError(f"Something wrong with sorted matches: {sorted_matchs}")

with open(true_input,'r') as f:

    pass

print(f"part 1 = {ans}")
