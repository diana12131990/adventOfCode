import re

f = open("day_1_input.txt","r")

line = f.readline()
line = line.strip()
line = re.findall("\d",line)

total = 0
for i in range(len(line)):
    if i != len(line) - 1:
        j = i+1
    else:
        j = 0
    
    if line[i] == line[j]:
        total += int(line[i])

print(total)