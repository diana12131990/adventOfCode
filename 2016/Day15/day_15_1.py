import re

f = open("day_15_input.txt","r")

discs = []
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    discs.append([int(numbers[0]),int(numbers[1]),int(numbers[3])])
    
f.close()

t = 0
while True:
    last_pos = -1
    Skip = False
    for d in discs:
        pos = (t + d[0] + d[2])%d[1]
        if last_pos == -1:
            last_pos = pos
        else:
            if last_pos != pos:
                Skip = True
                break
    if not Skip:
        break
    t += 1

print(t)    