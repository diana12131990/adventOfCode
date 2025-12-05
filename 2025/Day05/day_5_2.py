
import re

f = open("day_5_input.txt","r")

fresh_ranges_original = []
for line in f:
    line = line.strip()
    if line == "":
        break
        
    start, end = line.split('-')
    fresh_ranges_original.append([int(start),int(end)])

f.close()

fresh_ranges_original.sort(key=lambda x:[x[0],x[1]])
fresh_ranges_merged = []
for start, end in fresh_ranges_original:
    if not fresh_ranges_merged or start > fresh_ranges_merged[-1][1] + 1:
        fresh_ranges_merged.append([start,end])
    else:
        fresh_ranges_merged[-1][1] = max(fresh_ranges_merged[-1][1], end)

#print(fresh_ranges_original)
#print(fresh_ranges_merged)

total_fresh = 0
for start, end in fresh_ranges_merged:
    total_fresh += (end - start + 1)

print(total_fresh)
