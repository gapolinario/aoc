import os
import re

day = 12

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

# given a string without errors (?)
# and a list of contiguous errors
# return True if the string and the list of errors
# are compatible, and False otherwise
def string_matches_sharps(string,sharps):

    if '?' in string:
        raise ValueError(f"string should not contain `?`")

    pat = r'\.*'
    for s in sharps[:-1]:
        pat += r''.join([r'#' for _ in range(s)])
        pat += r'\.+'

    # last item
    s = sharps[-1]
    pat += r''.join([r'#' for _ in range(s)])
    pat += r'\.*'

    return re.match(pat,string) != None

def two_string_match(stringa,stringb):

    assert(len(stringa)==len(stringb))

    out = True
    for a,b in zip(stringa,stringb):
        out = out and not (a == '#' and b == '.')
        out = out and not (a == '.' and b == '#')

    return out

def number_to_base(n, b, num_digits):
    if n == 0:
        return [0 for _ in range(num_digits)]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b

    digits.extend([0 for _ in range(num_digits-len(digits))])
    return digits[::-1]

ans = 0

# say len(string) = la, len(sharps) = lb, sum(sharps) = sb,
# the actual string may be arranged as
# with a number of paddings, where the first and last can be zero,
# the middle ones cannot, so we have
#
# (1,1,3) = __ # __ # __ ### ___
#           (l1) (l2) (l3)   (l4)
#
# 0 <= l1 <= la - sb - 2
# 1 <= l2 <= la - sb - 1
# 1 <= l3 <= la - sb - 1
# 0 <= l4 <= la - sb - 2
# and we know that
# sb + l1 + l2 + l3 + l4 = la
# the only solution to this is l1,l2,l3,l4 = 0,1,1,0
# on the true input, none of the lines have a single solution,
# see test below

with open(test_input,'r') as f:
    
    assert(string_matches_sharps('#.#.###',[1,1,3]))

    if False:
        # for test input, tot = 7346
        # for true input, tot = 10 058 184
        # 10 million, can be brute forced

        tot = 0
        for l in f:
            l1,l2 = re.split(r' ',l)
            sharps = [ int(x) for x in re.split(r',',l2[:-1]) ]
            #if len(l1) == sum(sharps)+len(sharps)-1:
            
            # find max number of solutions for brute force search is
            # max val - min val + 1
            ua = (len(l1) - sum(sharps) - (len(sharps) - 1)) - 0 + 1
            ub = (len(l1) - sum(sharps) - (len(sharps) - 2)) - 1 + 1
            ptot = ua**2 * ub**(len(sharps)-1)
            print(f"{len(l1)} {sharps}, partial tot={ptot}")
            tot += ptot
        print(f"total = {tot}")

    for l in f:
        l1,l2 = re.split(r' ',l)
        sharps = [ int(x) for x in re.split(r',',l2[:-1]) ]

        # base
        b = len(l1) - sum(sharps) - len(sharps) + 2
        #print(b)

        stringa = l1
        
        # brute force search
        # convert index to base b first
        for i in range(b**(len(sharps)+1)):

            digits = number_to_base(i,b,len(sharps)+1)

            for j in range(1,len(digits)-1):
                digits[j] += 1
            # first and last digits go from 0 to b-1
            # all other digits go from 1 to b

            stringb = ''
            for j in range(len(sharps)):
                stringb += ''.join(['.' for _ in range(digits[j])])
                stringb += ''.join(['#' for _ in range(sharps[j])])

            # extra space in the end
            stringb += ''.join(['.' for _ in range(digits[-1])])

            assert(sum(sharps)+sum(digits)==len(stringb))

            if sum(sharps) + sum(digits) == len(stringa):
                if two_string_match(stringa,stringb):
                    ans += 1
                    #print(f"{stringa} {sharps} {digits} {stringb}")

print(f"part 1 = {ans}")

ans = 0

with open(test_input,'r') as f:
    
    if True:
        # for test input, tot = 7346
        # for true input, tot = 10 058 184
        # 10 million, can be brute forced

        tot = 0
        for l in f:
            l1,l2 = re.split(r' ',l)
            sharps = [ int(x) for x in re.split(r',',l2[:-1]) ]
            #if len(l1) == sum(sharps)+len(sharps)-1:
            
            # find max number of solutions for brute force search is
            # max val - min val + 1
            u = (len(l1) - sum(sharps) - (len(sharps) - 1)) - 0 + 1
            ptot = (5*u)**(5*len(sharps)+1)
            print(f"{len(l1)} {sharps}, partial tot={ptot}")
            tot += ptot
        print(f"total = {tot}")

    """
    for l in f:
        l1,l2 = re.split(r' ',l)
        sharps = [ int(x) for x in re.split(r',',l2[:-1]) ]

        # base
        b = len(l1) - sum(sharps) - len(sharps) + 2
        #print(b)

        stringa = l1
        
        # brute force search
        # convert index to base b first
        for i in range(b**(len(sharps)+1)):

            digits = number_to_base(i,b,len(sharps)+1)

            for j in range(1,len(digits)-1):
                digits[j] += 1
            # first and last digits go from 0 to b-1
            # all other digits go from 1 to b

            stringb = ''
            for j in range(len(sharps)):
                stringb += ''.join(['.' for _ in range(digits[j])])
                stringb += ''.join(['#' for _ in range(sharps[j])])

            # extra space in the end
            stringb += ''.join(['.' for _ in range(digits[-1])])

            assert(sum(sharps)+sum(digits)==len(stringb))

            if sum(sharps) + sum(digits) == len(stringa):
                if two_string_match(stringa,stringb):
                    ans += 1
                    #print(f"{stringa} {sharps} {digits} {stringb}")
    """

print(f"part 2 = {ans}")