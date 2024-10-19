import os
import re
import numpy as np

day = 2

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example1.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

def re_search_to_int(re_match):
    if re_match == None:
        return 0
    else:
        return int(re_match.group(1))

## part 1

ans = 0

# valid games with
# 12 red cubes, 13 green cubes, and 14 blue cubes

with open(true_input,'r') as f:
    for i in f:
        rounds = re.split(';|:',i)
        id = re.search(r'Game (\d+)', i)
        #print(f"Game {id.group(1)}")
        possible = True
        for round in rounds[1:]:
            r = re_search_to_int(re.search(r'(\d+) red', round))
            g = re_search_to_int(re.search(r'(\d+) green', round))
            b = re_search_to_int(re.search(r'(\d+) blue', round))
            #print(f"{r} red, {g} green, {b} blue")
            possible = possible and (r <= 12 and g <= 13 and b <= 14 and r+g+b <= 39)
        ans += int(id.group(1)) if possible else 0

print(f"part 1 = {ans}")

## part 2

ans = 0

with open(true_input,'r') as f:
    for i in f:
        rounds = re.split(';|:',i)
        id = re.search(r'Game (\d+)', i)
        possible = True
        # 3 is just a rough bound on the number of rounds
        rlist = []
        for round in rounds[1:]:
            r = re_search_to_int(re.search(r'(\d+) red', round))
            g = re_search_to_int(re.search(r'(\d+) green', round))
            b = re_search_to_int(re.search(r'(\d+) blue', round))
            rlist.append([r,g,b])
        rlist = np.array(rlist)
        power = max(rlist[:,0]) * max(rlist[:,1]) * max(rlist[:,2])
        ans += power

print(f"part 2 = {ans}")

## part 2

# from savbell, avoiding numpy

ans = 0

with open(true_input,'r') as f:
    for i in f:
        rounds = re.split(';|:',i)
        id = re.search(r'Game (\d+)', i)
        possible = True
        rlist = {'red': [], 'blue': [], 'green': []}
        for round in rounds[1:]:
            r = re_search_to_int(re.search(r'(\d+) red', round))
            g = re_search_to_int(re.search(r'(\d+) green', round))
            b = re_search_to_int(re.search(r'(\d+) blue', round))
            rlist['red'].append(r)
            rlist['green'].append(g)
            rlist['blue'].append(b)
        power = max(rlist['red']) * max(rlist['blue']) * max(rlist['green'])
        ans += power

print(f"part 2 = {ans}")