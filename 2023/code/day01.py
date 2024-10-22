import os
import re
import numpy as np

day = 1

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

def minus_to_max(x,max=1000):
    if x < 0:
        return max
    else:
        return x

def minus_to_min(x,abs_min=1000):
    if x < 0:
        return -abs_min
    else:
        return x

## part 1

ans = 0

with open(true_input,'r') as f:
    for i in f:
        a = re.findall('(\d)',i)
        ans += 10 * int(a[0]) + int(a[-1])

print(f"part 1 = {ans}")

## part 2

spelled_digits = ['one','two','three','four','five','six','seven','eight','nine']

ans = 0

with open(true_input,'r') as f:
    
    for i in f:

        line = i

        first_spelled_digit = [ minus_to_max(line.find(spelled_digit)) for spelled_digit in spelled_digits ]

        digit_a = np.argmin(first_spelled_digit)

        last_spelled_digit  = [ len(line) - len(spelled_digit) - 
        minus_to_max(line[::-1].find(spelled_digit[::-1])) for spelled_digit in spelled_digits ]

        digit_b = np.argmax(last_spelled_digit)

        linea = re.sub(spelled_digits[digit_a],str(digit_a+1),line)
        lineb = re.sub(spelled_digits[digit_b],str(digit_b+1),line)

        a = re.findall('(\d)',linea)
        b = re.findall('(\d)',lineb)
        ans += 10 * int(a[0]) + int(b[-1])

        #print(f"{line} => {a} => {10 * int(a[0]) + int(b[-1])}")

print(f"part 2 = {ans}")

# https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
# hint from reddit
# two more examples, then the test case adds up to 443

## part 2

# with help from lookahead regex and
# this one liner
# https://github.com/savbell/advent-of-code-one-liners/blob/master/2023/day-01.py

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    }

ans = 0

with open(true_input,'r') as f:
    
    for i in f:

        a = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',i)
        v = ''.join([digits[x] if x.isalpha() else x for x in [a[0],a[-1]]])
        ans += int(v)

print(f"part 2 = {ans}")
