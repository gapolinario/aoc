import os
import re
import numpy as np

day = 3

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"
test_input2 = f"../input/{day:02d}_example2.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

def issymb(x):

    return x != '.' and not x.isdigit()

def read_line_i(f,i):
    f.seek(0)
    for linei, line in enumerate(f):
        if linei == i:
            return line  # Return the desired line

## part 1

ans = 0

with open(true_input,'r') as f:

    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    d1 = len(t1)
    d2 = len(t1[0])

    t = np.empty((d1,d2),dtype=str)
    for li,ti in enumerate(t1):
        t[li,:] = np.array([ x for x in ti])
    del t1

    for i,li in enumerate(f):
        a = re.finditer(r'(\d+)',li)
        for b in a:
            #print(f"{b.start(1)}, {i[b.start(1)]}, {b.end(1)}, {i[b.end(1)]}")
            # symbol at the left
            isgear = b.start(1) != 0 and issymb(li[b.start(1)-1])
            # symbol at the right
            isgear = isgear or ( b.end(1) != d2 and issymb(li[b.end(1)]) )
            # symbol on top
            if i != 0:
                isgear = isgear or any( issymb(t[i-1,v]) for v in range(b.start(1),b.end(1)) )
            # symbol at bottom
            if i != d1-1:
                isgear = isgear or any( issymb(t[i+1,v]) for v in range(b.start(1),b.end(1)) )
            # symbol at upper left diagonal
            if b.start(1) != 0 and i != 0:
                isgear = isgear or issymb(t[i-1,b.start(1)-1])
            # symbol at lower left diagonal
            if b.start(1) != 0 and i != d1-1:
                isgear = isgear or issymb(t[i+1,b.start(1)-1])
            # symbol at upper right diagonal
            if b.end(1) != d2 and i != 0:
                isgear = isgear or issymb(t[i-1,b.end(1)])
            # symbol at lower right diagonal
            if b.end(1) != d2 and i != d1-1:
                isgear = isgear or issymb(t[i+1,b.end(1)])
            if isgear:
                #print(b.group(1))
                ans += int(b.group(1))

print(f"part 1 = {ans}")

# error: left and right corners do not count as symbols, obviously

## part 2

ans = 0

with open(true_input,'r') as f:

    t1 = np.loadtxt(f.name,dtype=str,comments=None)

    d1 = len(t1)
    d2 = len(t1[0])

    t = np.empty((d1,d2),dtype=str)
    for li,ti in enumerate(t1):
        t[li,:] = np.array([ x for x in ti])
    del t1

    # find all *
    gears = []
    for i in range(d1):
        for j in range(d2):
            if t[i,j] == '*':
                gears.append([i,j])

    #print(f"gears = {gears}")

    for i,j in gears:

        neighbors = []
        # number at the left
        if j != 0:
            if t[i,j-1].isdigit():
                neighbors.append([i,j-1])
        # number at the right
        if j != d2-1:
            if t[i,j+1].isdigit():
                neighbors.append([i,j+1])
        # number on top
        if i != 0:
            if t[i-1,j].isdigit():
                neighbors.append([i-1,j])
        # number at bottom
        if i != d1-1:
            if t[i+1,j].isdigit():
                neighbors.append([i+1,j])
        # number at upper left diagonal
        if j != 0 and i != 0:
            if t[i-1,j-1].isdigit():
                neighbors.append([i-1,j-1])
        # number at lower left diagonal
        if j != 0 and i != d1-1:
            if t[i+1,j-1].isdigit():
                neighbors.append([i+1,j-1])
        # number at upper right diagonal
        if j != d2-1 and i != 0:
            if t[i-1,j+1].isdigit():
                neighbors.append([i-1,j+1])
        # number at lower right diagonal
        if j != d2-1 and i != d1-1:
            if t[i+1,j+1].isdigit():
                neighbors.append([i+1,j+1])
        #ans += int(b.group(1))

        if len(neighbors) < 2:
        # only 1 neighbor, is not a gear
            continue
    
        #print(f"possible gear at: {i} {j}")
        #print(f"neighbors={neighbors}")

        # anki: iterators are exhausted

        number_neighbors = []
        for neigh in neighbors:
            l = read_line_i(f,neigh[0]) if i != 0 else None
            nums = re.finditer(r'(\d+)',l)
            for num in nums:
                if neigh[1] >= num.start() and neigh[1] < num.end():
                    number_neighbors.append([num.group(1),num.start(1),num.end(1)])    

        #print(f"possible gear at: {i} {j}")
        #print(f"all neighbors = {number_neighbors}")

        unique_neighbors = []
        for ai,a in enumerate(number_neighbors):
            is_unique = True
            for b in number_neighbors[ai+1:]:
                test = a[0] != b[0] or a[1] != b[1] or a[2] != b[2]
                is_unique = is_unique and test
            if is_unique:
                unique_neighbors.append(a)

        #print(f"unique neighbors={unique_neighbors}")

        if len(unique_neighbors) == 2:
            ans += int(unique_neighbors[0][0]) * int(unique_neighbors[1][0])

print(f"part 2 = {ans}")
