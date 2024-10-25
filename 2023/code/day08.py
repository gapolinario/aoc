import os
import re
from math import lcm

day = 8

true_input = f"../input/{day:02d}.dat"
test_input1 = f"../input/{day:02d}_example1.dat"
test_input2 = f"../input/{day:02d}_example2.dat"
test_input3 = f"../input/{day:02d}_example3.dat"

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

def end_site_q(site):
    end = True
    for a in site:
        end = end and (re.match(r'\w\wZ',a) != None)
    return end

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

    # brute force
    # ans = 10 371 555 451 871
    # would take a loooong time,
    # even in a compiled language
    if False:

        # start sites
        sites = []
        f.seek(0)
        for l in f:
            l0 = re.search(r'^(\w\wA) = ',l)
            if l0 != None:
                sites.append(l0.group(1))

        while not end_site_q(sites):
            for i,a in enumerate(sites):
                side = step[instructions[ans%num_instructions]]
                sites[i] = the_map[a][side]
            ans += 1

    print(f"part 2, brute force = {ans}")

    ans = 0

    # sadly I got a spoiler from reddit: just find Z and use LCM
    if True:

        # start sites
        sites = []
        f.seek(0)
        for l in f:
            l0 = re.search(r'^(\w\wA) = ',l)
            if l0 != None:
                sites.append(l0.group(1))

        steps = {}
        for site in sites:
            steps[site] = 0

        for init_site in sites:

            site = init_site
            site_ans = 0
            while re.match(r'\w\wZ',site) == None:
                side = step[instructions[site_ans%num_instructions]]
                site = the_map[site][side]
                site_ans += 1
            steps[init_site] = site_ans

        print(steps)
        ans = lcm(*steps.values())

print(f"part 2 = {ans}")
