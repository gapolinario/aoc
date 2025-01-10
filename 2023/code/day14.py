import os
import re
import numpy as np
import matplotlib.pyplot as plt

day = 14

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

def pretty_print(t):
    for l in t:
        print(''.join([a for a in l]))

def slide_north(t):
    
    dy,dx = t.shape

    for i in range(dx):
        fallto = -1
        for j in range(dy):
            if t[j,i] == '#':
                fallto = j
            elif t[j,i] == 'O' and j == fallto + 1:
                fallto = j
            elif t[j,i] == 'O' and j > fallto+1:
                t[fallto+1,i] = 'O'
                t[j,i] = '.'
                fallto += 1

    return t

def slide_west(t):
    
    dy,dx = t.shape

    for j in range(dy):
        fallto = -1
        for i in range(dx):
            if t[j,i] == '#':
                fallto = i
            elif t[j,i] == 'O' and i == fallto + 1:
                fallto = i
            elif t[j,i] == 'O' and i > fallto+1:
                t[j,fallto+1] = 'O'
                t[j,i] = '.'
                fallto += 1

    return t

def slide_south(t):
    
    dy,dx = t.shape

    for i in range(dx):
        fallto = dy
        for j in range(dy-1,-1,-1):
            if t[j,i] == '#':
                fallto = j
            elif t[j,i] == 'O' and j == fallto-1:
                fallto = j
            elif t[j,i] == 'O' and j < fallto-1:
                t[fallto-1,i] = 'O'
                t[j,i] = '.'
                fallto -= 1

    return t

def slide_east(t):
    
    dy,dx = t.shape

    for j in range(dy):
        fallto = dx
        for i in range(dx-1,-1,-1):
            if t[j,i] == '#':
                fallto = i
            elif t[j,i] == 'O' and i == fallto-1:
                fallto = i
            elif t[j,i] == 'O' and i < fallto-1:
                t[j,fallto-1] = 'O'
                t[j,i] = '.'
                fallto -= 1

    return t

def compute_load(t):

    dy,dx = t.shape
    load = 0

    for i,l in enumerate(t):
        load += sum([x=='O' for x in l]) * (dy-i)

    return load 

ans = 0

with open(true_input,'r') as f:

    t = []
    for l in f:
        t.append([x for x in l[:-1]])
    t = np.array(t)

    t = slide_north(t)
    
    ans = compute_load(t)

print(f"part 1 = {ans}")

ans = 0

with open(true_input,'r') as f:

    t = []
    for l in f:
        t.append([x for x in l[:-1]])
    t = np.array(t)

    # this was used to verify how many steps
    # we need to reach the periodic state
    # 400 is enough for the true input
    if True:

        partl_steps = 400
        all_l = np.empty(partl_steps,dtype=int)

        for i in range(partl_steps):

            t = slide_north(t)
            t = slide_west(t)
            t = slide_south(t)
            t = slide_east(t)

            l = compute_load(t)
            all_l[i] = l

        #plt.plot(range(partl_steps),all_l)
        #plt.show()
        #plt.close()

        #fig,ax = plt.subplots(1,1)
        #ax.plot(range(300,330),all_l[300:330])
        #ax.set_xticks(range(300,330))
        #plt.show()
        #plt.close()

        """
        period = 0
        i = 330
        l0 = all_l[300]
        while period == 0:
            if all_l[i] == l0:
                period = i-300
            else:
                i -= 1

        print(period)
        print(all_l[300:300+period])

        assert(all_l[300] == all_l[300+period])
        """

    # test, period = 7
    period = 26
    cycles = 1000000000
    #cycles = 326
    n = (cycles - 300) % period
    ans = all_l[300+n-1]
    
print(f"part 2 = {ans}")

# 105154, too high, probably off by one
# 105060, still too high
# 105008
# just notice that a300 = a326 = a352 = a378

