import os
import re
import math as m

day = 6

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 1

def travel_distance(t_hold,t_race):
    assert(t_race >  0)
    assert(t_hold >= 0)
    assert(t_hold <= t_race)
    # speed = t_hold
    # distance = t_remain * speed
    return (t_race - t_hold) * t_hold

def get_hold_times(t_race,record_dist):

    t1 = 0.5 * (t_race - m.sqrt(t_race**2 - 4*record_dist))
    t2 = 0.5 * (t_race + m.sqrt(t_race**2 - 4*record_dist))

    t1 = max([0,int(m.floor(t1))])
    t2 = min([t_race-1,int(m.floor(t2))])

    if travel_distance(t1,t_race) == record_dist:
        t1 += 1
    #if travel_distance(t2,t_race) == record_dist:
    #    pass

    assert( t1 < t2 )

    return t1,t2

with open(true_input,'r') as f:

    # array of total race times
    t_array = [ int(x) for x in re.findall(r'(\d+)',f.readline())]
    # array of record distances
    r_array = [ int(x) for x in re.findall(r'(\d+)',f.readline())]

    for t,r in zip(t_array,r_array):

        # multiplicity = number of solutions
        # to travel_dist > record_travel_dist
        t1,t2 = get_hold_times(t,r)

        mult = t2-t1
        print(t1,t2,mult)

        ans *= mult

print(f"part 1 = {ans}")

## part 2

ans = 0

with open(true_input,'r') as f:

    # array of total race times
    t_race = int(''.join(re.findall(r'(\d+)',f.readline())))
    # array of record distances
    record_dist = int(''.join(re.findall(r'(\d+)',f.readline())))

    # multiplicity = number of solutions
    # to travel_dist > record_travel_dist
    t1,t2 = get_hold_times(t_race,record_dist)

    ans = t2-t1

print(f"part 2 = {ans}")
