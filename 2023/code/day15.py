import os
import re

day = 15

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

# char to ascii int: ord('a') (returns 97)
# ascii int to char: chr(97) (returns 'a')

ans = 0

def hash(s):

    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
        #print(f"{c} {ord(c)} {val}")

    return val

with open(true_input,'r') as f:

    assert(hash('HASH')==52)

    l = re.split(',',f.readline())
    for a in l:
        #print(hash(a))
        ans += hash(a)

print(f"part 1 = {ans}")

ans = 0

with open(test_input,'r') as f:

    # all boxes, inside there's an array with lens label and focal length
    boxes = {}
    # all boxes, list of labels inside each box, unordered
    lenses = {}

    l = re.split(',',f.readline())
    for a in l:
        
        if   a.find('=') >= 0:
            label, foclen = re.split(r'=',a)
            boxno = hash(label)
            if boxno in boxes.keys():
                if label in lenses[boxno]: # replace
                    i = 0
                    while False:
                        pass
                    boxes[boxno][i] = [label,foclen]
                    # lenses[boxno] does not change
                else:
                    boxes[boxno].append([label,foclen])
                    lenses[boxno].append(label)
            else: # add lens
                boxes[boxno]  = [label,foclen]
                lenses[boxno] = [label]
        elif a.find('-') >= 0:
            label, _ = re.split(r'-',a)
            boxno = hash(label)
            if boxno in boxes.keys():
                if label in lenses[boxno]: # remove
                    pass
                else:
                    pass
                    # do nothing
            else:
                pass # do nothing
        else:
            raise ValueError(f"Invalid instruction: {a}")

    print(boxes)

print(f"part 2 = {ans}")
