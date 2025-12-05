
import re

f = open("day_5_input.txt","r")

fresh_ranges_check = []
getting_range = True
total_fresh = 0
for line in f:
    line = line.strip()
    if line == "":
        getting_range = False
        
    else:
        if getting_range:
            start, end = line.split('-')
            fresh_ranges_check.append([int(start),int(end)])
            
        else:
            is_fresh = False
            for fresh_range in fresh_ranges_check:
                if fresh_range[0] <= int(line) <= fresh_range[1]:
                    is_fresh = True
                    break
                
            if is_fresh:
                total_fresh += 1

f.close()

print(total_fresh)
