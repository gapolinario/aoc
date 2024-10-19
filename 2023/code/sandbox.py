import re

test_input = f"../input/sandbox.dat"

with open(test_input,'r') as f:

    l = []
    for i in f:
        it = re.finditer(r'(\d+)',i)

    for i in it:
        print(i.group(1))

    for i in it:
        print(i.group(1))