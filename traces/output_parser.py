import re

pattern_load_factor = "load factor is: ([0-9.]+)"
pattern_wall_clock = "real\s+\d+m([0-9.]+)"

with open("output_dramsim.txt", "r") as output_file:
    text = output_file.read()

    load_factors = re.findall(pattern_load_factor, text)
    wall_clocks = re.findall(pattern_wall_clock, text)

    # for load_factor in load_factors:
    #     print (load_factor)
    #
    # for wall_clock in wall_clocks:
    #     print (wall_clock)
    
    # Determine the lenth, wall clock is the second parameter
    common_length = len(wall_clocks)
    for counter, wall_clock in enumerate(wall_clocks):
        print ("%s %s" % (load_factors[counter], wall_clock ))
