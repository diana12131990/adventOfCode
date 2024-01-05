import re

f = open("day_2_input.txt","r")

total_paper_size = 0
for line in f:
    line = line.strip()
    lengths = re.split("x",line)
    lengths = [int(x) for x in lengths]
    lengths.sort()
    total_paper_size += 3 * lengths[0] * lengths[1] + 2 * lengths[1] * lengths[2] + 2 * lengths[0] * lengths[2]

f.close()

print(total_paper_size)