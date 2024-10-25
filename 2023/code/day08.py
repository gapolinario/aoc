import os
import re
import numpy as np

day = 8

true_input = f"../input/{day:02d}.dat"
test_input1 = f"../input/{day:02d}_example1.dat"
test_input2 = f"../input/{day:02d}_example2.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

with open(true_input,'r') as f:

    step = {'L': 0, 'R': 1}

    instructions = f.readline()[:-1]
    num_instructions = len(instructions)
    the_map = {}

    f.readline()
    for l in f:
        l0 = re.search(r'^(\w+) = ',l).group(1)
        l1 = re.search(r'\((\w+)',l).group(1)
        l2 = re.search(r'(\w+)\)',l).group(1)
        the_map[l0] = [l1,l2]

    site = 'AAA'
    while site != 'ZZZ':
        side = step[instructions[ans%num_instructions]]
        site = the_map[site][side]
        ans += 1

print(f"part 1 = {ans}")

## part 2

ans = 0

with open(test_input2,'r') as f:

    step = {'L': 0, 'R': 1}

    instructions = f.readline()[:-1]
    num_instructions = len(instructions)
    the_map = {}

    f.readline()
    for l in f:
        l0 = re.search(r'^(\w+) = ',l).group(1)
        l1 = re.search(r'\((\w+)',l).group(1)
        l2 = re.search(r'(\w+)\)',l).group(1)
        the_map[l0] = [l1,l2]

    site = 'AAA'
    while site != 'ZZZ':
        side = step[instructions[ans%num_instructions]]
        site = the_map[site][side]
        ans += 1

print(f"part 2 = {ans}")
