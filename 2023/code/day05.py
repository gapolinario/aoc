import os
import re
import numpy as np
#from numba import jit

day = 5

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

def get_fun_specs(f,loc_start,loc_end):

    assert( loc_start >= 0 )
    assert( loc_end > 0 )
    assert( loc_end > loc_start )

    f.seek(loc_start)
    f.readline() # skip one line, with name of function

    specs = []
    while f.tell() < loc_end-1:
        l = f.readline()
        specs.append([ int(x) for x in re.findall(r'(\d+)',l)])

    return np.array(specs)

def piecewise_linear_fun(x,fun):

    # fun is an M x 3 array

    for l in fun:
        if x >= l[1] and x < l[1] + l[2]:
            return l[0] + (x-l[1])
    
    # default case
    return x

def composite_seed_to_location(seed,fun_tensor):

    # fun_tensor is an array, each element is an M_a x 3 tensor

    loc = seed
    for a in fun_tensor:
        loc = piecewise_linear_fun(loc,a)

    return loc

with open(true_input,'r') as f:

    # last byte of file
    loc_end_f = f.seek(0,2)

    f.seek(0)

    seeds = [ int(x) for x in re.findall(r'(\d+)',f.readline())]
    locs  = np.empty_like(seeds)

    f.seek(0)

    s = f.read().replace('\n', ' ')

    loc_seed_to_soil            = s.find('seed-to-soil map:')
    loc_soil_to_fertilizer      = s.find('soil-to-fertilizer map:')
    loc_fertilizer_to_water     = s.find('fertilizer-to-water map:')
    loc_water_to_light          = s.find('water-to-light map:')
    loc_light_to_temperature    = s.find('light-to-temperature map:')
    loc_temperature_to_humidity = s.find('temperature-to-humidity map:')
    loc_humidity_to_location    = s.find('humidity-to-location map:')

    del s

    fun_seed_to_soil            = get_fun_specs(f,loc_seed_to_soil,loc_soil_to_fertilizer)
    fun_soil_to_fertilizer      = get_fun_specs(f,loc_soil_to_fertilizer,loc_fertilizer_to_water)
    fun_fertilizer_to_water     = get_fun_specs(f,loc_fertilizer_to_water,loc_water_to_light)
    fun_water_to_light          = get_fun_specs(f,loc_water_to_light,loc_light_to_temperature)
    fun_light_to_temperature    = get_fun_specs(f,loc_light_to_temperature,loc_temperature_to_humidity)
    fun_temperature_to_humidity = get_fun_specs(f,loc_temperature_to_humidity,loc_humidity_to_location)
    fun_humidity_to_location    = get_fun_specs(f,loc_humidity_to_location,loc_end_f)

    for i,seed in enumerate(seeds):

        loc = piecewise_linear_fun(seed,fun_seed_to_soil)
        loc = piecewise_linear_fun(loc,fun_soil_to_fertilizer)
        loc = piecewise_linear_fun(loc,fun_fertilizer_to_water)
        loc = piecewise_linear_fun(loc,fun_water_to_light)
        loc = piecewise_linear_fun(loc,fun_light_to_temperature)
        loc = piecewise_linear_fun(loc,fun_temperature_to_humidity)
        loc = piecewise_linear_fun(loc,fun_humidity_to_location)
        
        locs[i] = loc

    ans = min(locs)

print(f"part 1 = {ans}")

## part 2

ans = 0

with open(true_input,'r') as f:

    # last byte of file
    loc_end_f = f.seek(0,2)

    f.seek(0)

    # question: Does (\d+)\s+(\d+) work? because the cursor advances in pairs
    seeds_line = [ int(x) for x in re.findall(r'(\d+)',f.readline()) ]
    
    seed_pairs = np.empty((len(seeds_line)//2,2),dtype=int)
    for i in range(len(seeds_line)//2):
        seed_pairs[i,:] = [seeds_line[2*i], seeds_line[2*i+1]]
        # below, the naive approach
        # this breaks because the number of seeds is huge
        #seeds.extend(range(seed_pairs[2*i],seed_pairs[2*i]+seed_pairs[2*i+1]))

    locs  = np.empty((len(seeds_line)//2,),dtype=int)

    f.seek(0)

    s = f.read().replace('\n', ' ')

    loc_seed_to_soil            = s.find('seed-to-soil map:')
    loc_soil_to_fertilizer      = s.find('soil-to-fertilizer map:')
    loc_fertilizer_to_water     = s.find('fertilizer-to-water map:')
    loc_water_to_light          = s.find('water-to-light map:')
    loc_light_to_temperature    = s.find('light-to-temperature map:')
    loc_temperature_to_humidity = s.find('temperature-to-humidity map:')
    loc_humidity_to_location    = s.find('humidity-to-location map:')

    del s

    fun_seed_to_soil            = get_fun_specs(f,loc_seed_to_soil,loc_soil_to_fertilizer)
    fun_soil_to_fertilizer      = get_fun_specs(f,loc_soil_to_fertilizer,loc_fertilizer_to_water)
    fun_fertilizer_to_water     = get_fun_specs(f,loc_fertilizer_to_water,loc_water_to_light)
    fun_water_to_light          = get_fun_specs(f,loc_water_to_light,loc_light_to_temperature)
    fun_light_to_temperature    = get_fun_specs(f,loc_light_to_temperature,loc_temperature_to_humidity)
    fun_temperature_to_humidity = get_fun_specs(f,loc_temperature_to_humidity,loc_humidity_to_location)
    fun_humidity_to_location    = get_fun_specs(f,loc_humidity_to_location,loc_end_f)

    max_seed = max([ x[1] + x[2] for x in fun_humidity_to_location ])
    print(max_seed)

    max_locs = max([ x[0] + x[2] for x in fun_humidity_to_location ])
    ans = max_locs + 1
    print(max_locs)

    fun_tensor = [fun_seed_to_soil,fun_soil_to_fertilizer,fun_fertilizer_to_water,
                    fun_water_to_light,fun_light_to_temperature,fun_temperature_to_humidity,
                    fun_humidity_to_location]

    # test composite function and fun tensor are correct
    if False:

        for seed in range(0,max_seed,1000):
            
            loc = piecewise_linear_fun(seed,fun_seed_to_soil)
            loc = piecewise_linear_fun(loc,fun_soil_to_fertilizer)
            loc = piecewise_linear_fun(loc,fun_fertilizer_to_water)
            loc = piecewise_linear_fun(loc,fun_water_to_light)
            loc = piecewise_linear_fun(loc,fun_light_to_temperature)
            loc = piecewise_linear_fun(loc,fun_temperature_to_humidity)
            loc = piecewise_linear_fun(loc,fun_humidity_to_location)

            assert( loc == composite_seed_to_location(seed,fun_tensor) )

    del fun_seed_to_soil
    del fun_soil_to_fertilizer
    del fun_fertilizer_to_water
    del fun_water_to_light
    del fun_light_to_temperature
    del fun_temperature_to_humidity
    del fun_humidity_to_location

    # test how long it would take to brute force it, up to 15h
    if False:

        for seed in range(max_seed//1000):
            
            loc = composite_seed_to_location(seed,fun_tensor)

    # runtime tests
    # max_seed = max_locs = 4 060 994 810
    # 4K = 4 * 10^3 function evaluations, 2s (experimental)
    # 4M = 4 * 10^6, 45s (experimental)
    # 4B = 4 * 10^9, up to 900 min = 15h

    # test how long it would take with a simpler function, 30 min
    if False:

        u = 0
        for seed in range(max_seed//1000):
            
            u += 1

    # runtime tests, with a simple function
    # 4M = 4 * 10^6, 2s (experimental)
    # 4B = 4 * 10^9, 

    # test how long it would take with a single piecewise function, about 2h
    if False:

        for seed in range(max_seed//1000):
            
            loc = piecewise_linear_fun(seed,fun_seed_to_soil)

    # runtime tests, single piecewise function
    # 4M = 4 * 10^6, 7s (experimental)
    # 4B = 4 * 10^9, 7000s = 2h

    if True:

        for a,b in seed_pairs:

            loca = composite_seed_to_location(a)
            locb = composite_seed_to_location(a+b)
            if locb == loca + b:
                pass


print(f"part 2 = {ans}")
