import re
import numpy

f = open("day_2_input.txt","r")

total_ribbon_length = 0
for line in f:
    line = line.strip()
    lengths = re.split("x",line)
    lengths = [int(x) for x in lengths]
    lengths.sort()
    total_ribbon_length += 2 * (lengths[0] + lengths[1]) + numpy.prod(lengths)
    
f.close()

print(total_ribbon_length)