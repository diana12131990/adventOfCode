import re

f = open("day_19_input.txt","r")

patterns = []
designs = []
patterns_finish = False
for line in f:
    line = line.strip()
    if line == "":
        patterns_finish = True
    else:
        if patterns_finish:
            designs.append(line)
        else:
            patterns = line.split(", ")
f.close()

towel_set = set(patterns)
possible_designs = 0
for design in designs:
    dp = [False] * (len(design) + 1)  # dp[i] will be True if a valid segment ending at i is found
    valid_segments = [0]

    for i in range(1, len(dp)):
        for j in valid_segments:
            if design[j:i] in towel_set:
                dp[i] = True
                break
        if dp[i]:  
            valid_segments.append(i)
    if dp[-1]:  # If the end of the string is reached in valid segments
        possible_designs += 1
        
print(possible_designs)