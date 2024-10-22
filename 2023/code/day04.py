import os
import re

day = 4

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

with open(true_input,'r') as f:

    for l in f:
        l1,l2 = l.split('|')
        l0,l1 = l1.split(':')
        wins = [ int(a) for a in re.findall(r'(\d+)',l1) ]
        bets = [ int(a) for a in re.findall(r'(\d+)',l2) ]
        #print(f"wins={wins}, bets={bets}")

        match = 0
        for w in wins:
            for b in bets:
                if w == b:
                    match += 1

        if match > 0:
            ans += 2**(match-1)

print(f"part 1 = {ans}")

# mistake: the number in "Game x" was being considered

## part 2

## auxiliary functions

def fib(n):

    assert( n >= 0)

    if   n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def get_copies(matches,copies,num_cards):

    assert(num_cards > -1)

    if num_cards == 0:
        return 0

    #print(f"all matches={matches}")

    # this assumes that the dict keys of matches and copies
    # are numbers in order, always increasing by one
    # this also means no recursion is needed
    for key,val in matches.items():
        if val > 0:
            for i in range(key+1,min(key+val,num_cards)+1):
                copies[i] += copies[key]

    #print(f"all copies={copies}")

    return sum(copies.values())

## the code

ans = 0

with open(true_input,'r') as f:

    matches = {}
    copies  = {}
    for l in f:

        l1,l2 = l.split('|')
        l0,l1 = l1.split(':')

        id = int(re.search(r'Card\s+(\d+):',l).group(1))

        copies[id] = 1
        
        wins = [ int(a) for a in re.findall(r'(\d+)',l1) ]
        bets = [ int(a) for a in re.findall(r'(\d+)',l2) ]
        #print(f"wins={wins}, bets={bets}")

        match = 0
        for w in wins:
            for b in bets:
                if w == b:
                    match += 1

        if match > 0:
            matches[id] = match
        else:
            matches[id] = 0

    # last line
    num_cards = id
    #print(id)

    ans = get_copies(matches,copies,num_cards)

    #for key,val in copies.items():
    #   ans += val

print(f"part 2 = {ans}")

# mistake: the number in Game x was being considered

