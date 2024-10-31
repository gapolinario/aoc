import os
import re
import numpy as np

day = 13

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"
test_input2 = f"../input/{day:02d}_example2.dat"
test_input3 = f"../input/{day:02d}_example3.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

def pretty_print(t):

    for l in t:
        print(''.join([a for a in l]))

ans = 0

with open(true_input,'r') as f:
    
    s = f.read()
    s = re.finditer(r'\n\n',s)
    g1 = [0]
    for i in s:
        g1.append(i.end())
    g2 = g1[1:]
    g2.append(f.tell())

    #print(len(g1))

    # loop through each block
    for gi,gn in zip(g1,g2):
        
        f.seek(gi)
        t = []
        while f.tell() < gn-1:
            #print([x for x in f.readline().replace('\n','')])
            t.append([x for x in f.readline().replace('\n','')])
        t = np.array(t)

        #print(t)

        ax,ay = 0,0
        dy,dx = t.shape

        allx = []
        ally = []

        # loop over lines, horizontal reflection
        for i in range(1,dy):
        # greedy search, alternative 1
        #for i in np.concatenate((np.arange(dy//2,0,-1),np.arange(dy//2+1,dy-1))):
        # greedy search, alternative 2
        #for i in np.concatenate((np.arange(dy//2+1,0,-1),np.arange(dy//2+1,dy-1))):
            #print(f"axis of reflection: x {i}")
            #print(t[i:min(2*i,dy),:])
            #print(t[max(0,2*i-dy):i,:][::-1,:])
            if np.all(t[i:min(2*i,dy),:] == t[max(0,2*i-dy):i,:][::-1,:]):
                ax = i
                allx.append(ax)
                #print(f"axis of reflection: x {i}")
                #print(t[i:min(2*i,dy),:])
                #print(t[max(0,2*i-dy):i,:][::-1,:])
                #break

        # loop over lines, vertical reflection
        for i in range(1,dx):
        # greedy search, alternative 1
        #for i in np.concatenate((np.arange(dx//2,0,-1),np.arange(dx//2+1,dx-1))):
        # greedy search, alternative 2
        #for i in np.concatenate((np.arange(dx//2+1,0,-1),np.arange(dx//2+1,dx-1))):
            #print(f"axis of reflection: y {i}")
            #print(t[:,i:min(2*i,dx)])
            #print(t[:,max(0,2*i-dx):i][:,::-1])
            if np.all(t[:,i:min(2*i,dx)] == t[:,max(0,2*i-dx):i][:,::-1]):
                ay = i
                ally.append(ay)
                #print(f"axis of reflection: y {i}")
                #print(t[:,i:min(2*i,dx)])
                #print(t[:,max(0,2*i-dx):i][:,::-1])
                #break

        #if ax != 0 and ay != 0:
        #    pretty_print(t)
        #    raise InterruptedError("Two axis of rotation here!")

        #pretty_print([t[0,:]])
        #print(f"axis: {allx} {ally}")

        #print(f"{ax} {ay}")
        ans += 100 * ax + ay

print(f"part 1 = {ans}")

# mistake: going to dy-1, not to dy, now it works

ans = 0

def count_diffs(t1,t2):
    return np.sum([x1!=x2 for x1,x2 in zip(t1,t2)])

with open(true_input,'r') as f:
    
    s = f.read()
    s = re.finditer(r'\n\n',s)
    g1 = [0]
    for i in s:
        g1.append(i.end())
    g2 = g1[1:]
    g2.append(f.tell())

    # loop through each block
    for gi,gn in zip(g1,g2):
        
        f.seek(gi)
        t = []
        while f.tell() < gn-1:
            #print([x for x in f.readline().replace('\n','')])
            t.append([x for x in f.readline().replace('\n','')])
        t = np.array(t)

        #print(t)

        ax,ay = 0,0
        dy,dx = t.shape

        allx = []
        ally = []

        # loop over lines, horizontal reflection
        for i in range(1,dy):
            if count_diffs(t[i:min(2*i,dy),:],t[max(0,2*i-dy):i,:][::-1,:])==1:
                #print(f"x={i}")
                ax = i
                allx.append(ax)
        
        # loop over lines, vertical reflection
        for i in range(1,dx):
            if count_diffs(t[:,i:min(2*i,dx)],t[:,max(0,2*i-dx):i][:,::-1])==1:
                #print(f"y={i}")
                ay = i
                ally.append(ay)
        
        ans += 100 * ax + ay

print(f"part 2 = {ans}")