import re

f = open("day_1_input.txt","r")

line = f.readline()
line = line.strip()
line = re.findall("\d",line)

total = 0
for i in range(len(line)/2):
    j = i + len(line)/2
    if line[i] == line[j]:
        total += int(line[i])

total *= 2
print(total)