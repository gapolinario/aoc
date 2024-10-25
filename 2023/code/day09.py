import os
import re
from math import comb

day = 9

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

def list_to_coeffs(list):

    coeffs = [0] * len(list)

    for i,a in enumerate(list):
        a = list[i]
        for j in range(i):
            a -= comb(i,j) * coeffs[j]
        coeffs[i] = a

    return coeffs

def coeffs_to_next(coeffs,n):

    out = 0
    for i,a in enumerate(coeffs):
        out += comb(n,i) * a

    return out

with open(true_input,'r') as f:

    for l in f:
        s = [int(x) for x in re.split(r' ',l)]
        coeffs=list_to_coeffs(s)
        #print(f"list={s}")
        #print(f"coeffs={coeffs}")
        #print(f"ans={coeffs_to_next(coeffs,len(s))}")
        ans += coeffs_to_next(coeffs,len(s))

print(f"part 1 = {ans}")

# first try, 31045125580, too high
# there are negative numbers in the list
# in my first try, I had not defined coeffs to be
# initialized with zeros, once I did that, there was
# need to complicate, and the program always works

## part 2

ans = 0

with open(true_input,'r') as f:

    for l in f:
        s = [int(x) for x in re.split(r' ',l)]
        coeffs=list_to_coeffs(s)
        new = 0
        for i,a in enumerate(coeffs):
            new += (-1)**i * a
        #print(new)

        ans += new

print(f"part 2 = {ans}")
