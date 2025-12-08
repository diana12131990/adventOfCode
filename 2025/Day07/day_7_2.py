
import re
from collections import defaultdict

f = open("day_7_input.txt","r")

# Use defaultdict() to create list of integer to save the times
active_time = defaultdict(int)

# Get first line info
line = f.readline().strip()
active_time[line.find("S")] = 1

# Do the rest
for line in f:
    line = line.strip()
    
    new_active_time = defaultdict(int)
    for i,count in active_time.items():
        if line[i] == ".":
            new_active_time[i] += count
        elif line[i] == "^":
            if i-1 >= 0:
                new_active_time[i-1] += count
            if i+1 < len(line):
                new_active_time[i+1] += count
                
    active_time = new_active_time
f.close()

print(sum(active_time.values()))