import os
import re
import numpy as np

day = 10

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"
test_input2 = f"../input/{day:02d}_example2.dat"
test_input3 = f"../input/{day:02d}_example3.dat"
output = f"../output/{day:02d}.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

# the true input starts with (* = any tile)
# *7*
# 7S7
# *-*
# which means the loop starts from the top and ends 
# at the right

# unicode arrows:
# ←→↑↓

with open(true_input,'r') as f:

    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    d1 = len(t1)
    d2 = len(t1[0])

    # load input as array
    t = np.empty((d1,d2),dtype=str)
    for li,ti in enumerate(t1):
        # invert y direction, so that up means up
        t[d1-1-li,:] = np.array([ x for x in ti])
    del t1

    # s = starting position
    s = np.argwhere(t == 'S')
    assert(s.shape == (1,2))
    sy,sx = s[0]

    # step 0
    # p = current position
    py,px = sy,sx
    loop = [[sy,sx]]
    # arrow, points where I'm going, hard coded
    a  = '→'
    #print(f"step 0: p={d1-py,px+1}, a={a}")

    # step 1
    # this is hard coded to the true input, which
    # leaves from the right and joins back from the top
    py,px = sy,sx+1
    pz = t[py,px]
    assert(t[py,px]=='7')
    loop.append([py,px])
    a = '↓' 

    # steps 2 and so on
    #print(f"step 1: p={d1-py,px+1}, a={a}")
    while px != sx or py != sy:
        
        # walk in the direction
        # of the current arrow
        if   a == '↑':
            py,px = py+1,px
        elif a == '↓':
            py,px = py-1,px
        elif a == '→':
            py,px = py,px+1
        elif a == '←':
            py,px = py,px-1
        else:
            raise ValueError(f"arrow = {a}")

        pz = t[py,px]
        loop.append([py,px])

        #print(f"step x: p={d1-py,px+1}, a=x")

        # update arrow according to new site
        if   pz == '|' and a == '↑':
            a = '↑'
        elif pz == '|' and a == '↓':
            a = '↓'
        elif pz == '-' and a == '→':
            a = '→'
        elif pz == '-' and a == '←':
            a = '←'
        elif pz == 'L' and a == '←':
            a = '↑'
        elif pz == 'L' and a == '↓':
            a = '→'
        elif pz == 'J' and a == '→':
            a = '↑'
        elif pz == 'J' and a == '↓':
            a = '←'
        elif pz == '7' and a == '→':
            a = '↓'
        elif pz == '7' and a == '↑':
            a = '←'
        elif pz == 'F' and a == '←':
            a = '↓'
        elif pz == 'F' and a == '↑':
            a = '→'
        elif pz == 'S':
            pass
        else:
            # the input is already correct, and the loop
            # is connected, so I won't be checking too many things
            raise ValueError(f"Something wrong at p=({px},{py}) and a={a}")

        #print(f"step x: p={d1-py,px+1}, a={a}")

    ans = len(loop)//2

print(f"part 1 = {ans}")

ans = 0
part2 = True

def is_pipe(t):
    if t in ['F','L','J','7','-','|']:
        return True

def print_loop(loop,d1):

    for py,px in loop:
        print(f"[{d1-py} {px+1}]",end="")
    print()

with open(true_input,'r') as f:

    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    d1 = len(t1)
    d2 = len(t1[0])

    # load input as array
    t = np.empty((d1,d2),dtype=str)
    for li,ti in enumerate(t1):
        # invert y direction, so that up means up
        t[d1-1-li,:] = np.array([ x for x in ti])
    del t1

    # s = starting position
    s = np.argwhere(t == 'S')
    assert(s.shape == (1,2))
    sy,sx = s[0]

    # step 0
    # p = current position
    py,px = sy,sx
    loop = [[sy,sx]]
    # arrow, points where I'm going, hard coded
    a  = '→'
    rot = 0
    #print(f"step 0: p={d1-py,px+1}, a={a}")

    # step 1
    # this is hard coded to the true input, which
    # leaves from the right and joins back from the top
    py,px = sy,sx+1
    pz = t[py,px]
    assert(t[py,px]=='7')
    loop.append([py,px])
    a = '↓'
    rot -= 1
    # steps 2 and so on
    #print(f"step 1: p={d1-py,px+1}, a={a}")
    while px != sx or py != sy:
        
        # walk in the direction
        # of the current arrow
        if   a == '↑':
            py,px = py+1,px
        elif a == '↓':
            py,px = py-1,px
        elif a == '→':
            py,px = py,px+1
        elif a == '←':
            py,px = py,px-1
        else:
            raise ValueError(f"arrow = {a}")

        pz = t[py,px]
        loop.append([py,px])

        #print(f"step x: p={d1-py,px+1}, a=x")

        # update arrow according to new site
        if   pz == '|' and a == '↑':
            a = '↑'
        elif pz == '|' and a == '↓':
            a = '↓'
        elif pz == '-' and a == '→':
            a = '→'
        elif pz == '-' and a == '←':
            a = '←'
        elif pz == 'L' and a == '←':
            a = '↑'
            rot -= 1
        elif pz == 'L' and a == '↓':
            a = '→'
            rot += 1
        elif pz == 'J' and a == '→':
            a = '↑'
            rot += 1
        elif pz == 'J' and a == '↓':
            a = '←'
            rot -= 1
        elif pz == '7' and a == '→':
            a = '↓'
            rot -= 1
        elif pz == '7' and a == '↑':
            a = '←'
            rot += 1
        elif pz == 'F' and a == '←':
            a = '↓'
            rot += 1
        elif pz == 'F' and a == '↑':
            a = '→'
            rot -= 1
        elif pz == 'S':
            pass
        else:
            # the input is already correct, and the loop
            # is connected, so I won't be checking too many things
            raise ValueError(f"Something wrong at p=({px},{py}) and a={a}")

        #print(f"step x: p={d1-py,px+1}, a={a}, rot={rot}")

    # determine if rotation is clockwise or anticlockwise
    #if rot != 3 and rot != -3:
    #    raise ValueError(f"Invalid rotation value after one cycle. rot={rot}")

    #print_loop(loop,d1)

    for py in range(d1):
        for px in range(d2):
            # rename pipes that are not in the main loop
            in_loop = [py,px] in loop
            if not in_loop and is_pipe(t[py,px]):
                t[py,px] = ' '
            # rename pipes in the main loop
            #elif in_loop:
            #    t[py,px] = '■'

    # more hard coding: I know that rot = 5 in this example
    # so rot > 0 always
    assert(rot > 0)
    for py,px in loop:
        
        if   t[py,px] == 'L':
            if t[py+1,px+1] == '.':
                t[py+1,px+1] = '■'
        elif t[py,px] == 'F':
            if t[py-1,px+1] == '.':
                t[py-1,px+1] = '■'
        elif t[py,px] == '7':
            if t[py-1,px-1] == '.':
                t[py-1,px-1] = '■'
        elif t[py,px] == 'J':
            if t[py+1,px-1] == '.':
                t[py+1,px-1] = '■'

    # paint again, this is to aid visual inspection
    #for py in range(d1):
    #    for px in range(d2):
    #        if t[py,px] == '.':
    #            t[py,px] = '🟨'

    # print annotated grid
    with open(output,'w') as g:
        for l in reversed(t):
            g.write(''.join(l))
            g.write('\n')

    # determine the orientation of the loop

    # now I just have to search over the ground
    # then I use something like bucket fill

    # count number of I's
    #for py in range(d2):
    #    for px in range(d1):
    #        if t[py,px] == 'I':
    #            ans += 1

    for i in range(len(loop)):

        if i == len(loop)-1:
            # next
            pny,pnx = loop[0]
        else:
            pny,pnx = loop[i+1]
        # current
        p0y,p0x = loop[i]

        ans += (p0y+pny) * (p0x - pnx) / 2

    # this part was determined experimentally,
    # i had to remove the area of the loop,
    # approximately len(loop)/2, and to add 1 for
    # some reason. it worked
    ans -= len(loop)//2
    ans += 1

print(f"part 2 = {ans}")
