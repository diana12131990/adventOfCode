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

def calculate_ways(design, patterns, memo):
    if design in memo:
        return memo[design]
    total = 0 
    for pattern in patterns:
        if design.startswith(pattern):
            remaining_design = design[len(pattern):]
            if remaining_design:
                total += calculate_ways(remaining_design, patterns, memo)
            else:
                total += 1
    memo[design] = total
    return total

total_ways = 0
for design in designs:
    total_ways += calculate_ways(design, patterns, {})
print(total_ways)