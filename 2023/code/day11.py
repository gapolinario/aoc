import os
import re
import numpy as np

day = 11

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

def sign(x):
    return int( 2 * ( np.heaviside(x,1.0) - 0.5 ) )

# distance between galaxies g1 and g2
# given the space-time t
def get_dist(g1,g2,t,ex=2):

    g1y,g1x = g1
    g2y,g2x = g2
    dist = 0

    for i in range(g1y,g2y,sign(g2y-g1y)):
        if t[i,g1x] == '+':
            dist += ex
        else:
            dist += 1

    for i in range(g1x,g2x,sign(g2x-g1x)):
        if t[g2y,i] == '+':
            dist += ex
        else:
            dist += 1

    return dist

def print_table(t):
    for l in t:
        print(''.join(l))

with open(true_input,'r') as f:
    
    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    dy = len(t1)
    dx = len(t1[0])

    # load input as array
    t = np.empty((dy,dx),dtype=str)
    for li,ti in enumerate(t1):
        # invert y direction, so that up means up
        t[li,:] = np.array([ x for x in ti])
    del t1

    # before expansion, test distance function
    assert(get_dist([0,0],[2,2],t) == 4)
    assert(get_dist([0,0],[3,4],t) == 7)
    assert(get_dist([1,1],[1,1],t) == 0)

    for i in range(dy):
        l1 = t[i,:]
        if '#' not in l1:
            t[i,:] = np.full(dy,'+')

    for j in range(dx):
        l2 = t[:,j]
        if '#' not in l2:
            t[:,j] = np.full(dx,'+')

    galaxies = []
    for i in range(dy):
        for j in range(dx):
            if t[i,j] == '#':
                galaxies.append([i,j])

    galaxies = np.array(galaxies)

    if f.name == test_input:
        assert(get_dist(galaxies[4],galaxies[8],t)==9)
        assert(get_dist(galaxies[0],galaxies[6],t)==15)
        assert(get_dist(galaxies[2],galaxies[5],t)==17)
        assert(get_dist(galaxies[7],galaxies[8],t)==5)

    #print_table(t)

    for i,ga in enumerate(galaxies):
        for gb in galaxies[i+1:]:
            #print(f"dist {j} {ga} {gb} {get_dist(ga,gb,t)}")
            ans += get_dist(ga,gb,t)

print(f"part 1 = {ans}")

ans = 0

with open(true_input,'r') as f:

    ex = 1000000
    
    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    dy = len(t1)
    dx = len(t1[0])

    # load input as array
    t = np.empty((dy,dx),dtype=str)
    for li,ti in enumerate(t1):
        # invert y direction, so that up means up
        t[li,:] = np.array([ x for x in ti])
    del t1

    # before expansion, test distance function
    assert(get_dist([0,0],[2,2],t) == 4)
    assert(get_dist([0,0],[3,4],t) == 7)
    assert(get_dist([1,1],[1,1],t) == 0)

    for i in range(dy):
        l1 = t[i,:]
        if '#' not in l1:
            t[i,:] = np.full(dy,'+')

    for j in range(dx):
        l2 = t[:,j]
        if '#' not in l2:
            t[:,j] = np.full(dx,'+')

    galaxies = []
    for i in range(dy):
        for j in range(dx):
            if t[i,j] == '#':
                galaxies.append([i,j])

    galaxies = np.array(galaxies)

    for i,ga in enumerate(galaxies):
        for gb in galaxies[i+1:]:
            #print(f"dist {j} {ga} {gb} {get_dist(ga,gb,t)}")
            ans += get_dist(ga,gb,t,ex)

print(f"part 2 = {ans}")

# ans = 82000210, too low
# my mistake: I used the test input ...