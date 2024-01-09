import re

f = open("day_3_input.txt","r")

count = 0
t = [[],[],[]]
for line in f:
    line = line.strip()
    edge = re.findall("\d+",line)
    for i in range(3):
        t[i].append(int(edge[i]))
        
    if len(t[0]) == 3:
        for i in range(3):
            t[0].sort()
            if t[0][0] + t[0][1] > t[0][2]:
                count += 1
            t.pop(0)
            t.append([])
f.close()

print(count)