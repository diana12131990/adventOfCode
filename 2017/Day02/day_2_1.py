import re

f = open("day_2_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    numbers = [int(x) for x in numbers]
    
    total += max(numbers)-min(numbers)
    
print(total)
f.close()