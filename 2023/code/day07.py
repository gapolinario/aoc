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
    sorted_matchs = [] * 5
    for i,c in enumerate(matchs):
        minv = c
        mini = i
        for j,d in enumerate(matchs):
            if d < minv:
                minv  = d
                mini = j
        if mini != i:
            sorted_matchs[i] = minv
            sorted_matchs[mini] = c


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

    # array of total race times
    t_array = [ int(x) for x in re.findall(r'(\d+)',f.readline())]
    # array of record distances
    r_array = [ int(x) for x in re.findall(r'(\d+)',f.readline())]

    for t,r in zip(t_array,r_array):

        # multiplicity = number of solutions
        # to travel_dist > record_travel_dist
        t1,t2 = get_hold_times(t,r)

        mult = t2-t1
        print(t1,t2,mult)

        ans *= mult

print(f"part 1 = {ans}")
