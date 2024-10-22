import os
import re

day = 5

true_input = f"../input/{day:02d}.dat"
test_input = f"../input/{day:02d}_example.dat"

assert( os.path.basename(__file__) == f"day{day:02d}.py" )

## part 1

ans = 0

with open(test_input,'r') as f:

    s = f.read().replace('\n', ' ')

    loc_seed_to_soil            = s.find('seed-to-soil map:')
    loc_soil_to_fertilizer      = s.find('soil-to-fertilizer map:')
    loc_fertilizer_to_water     = s.find('fertilizer-to-water map:')
    loc_water_to_light          = s.find('water-to-light map:')
    loc_light_to_temperature    = s.find('light-to-temperature map:')
    loc_temperature_to_humidity = s.find('temperature-to-humidity map:')
    loc_humidity_to_location    = s.find('humidity-to-location map:')

    del s

    # use this to go to location in the file, then stay at next line
    f.seek(loc_seed_to_soil)
    print(f.readline())
    print(f.tell())

    #ans = min()


print(f"part 1 = {ans}")

