import re

f = open("day_3_input.txt","r")

count = 0

for line in f:
    line = line.strip()
    edge = re.findall("\d+",line)
    edge = [int(x) for x in edge]
    edge.sort()
    
    if edge[0] + edge[1] > edge [2]:
        count += 1
f.close()

print(count)