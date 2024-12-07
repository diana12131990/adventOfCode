import re

f = open("day_2_input.txt","r")

def isSafe(level):
    if not ((all(level[i] <= level[i + 1] for i in range(len(level) - 1))) or 
            (all(level[i] >= level[i + 1] for i in range(len(level) - 1)))):
        return False
    for i in range(len(level) - 1):
        if not (1 <= abs(level[i] - level[i + 1]) <= 3):
            return False 
    return True

safe_amount = 0
for line in f:
    level = re.findall(r'\d+', line)
    level = [int(i) for i in level]
    if isSafe(level):
        safe_amount += 1
f.close()
print(safe_amount)