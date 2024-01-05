import re

instructions = ["turn on","turn off","toggle"]

lights = []
for i in range(1000):
    lights.append([False] * 1000)

f = open("day_6_input.txt","r")

for line in f:
    line = line.strip()
    
    action = ""
    for x in instructions:
        if x in line:
            action = x
            break
        
    _,line = re.split(action + " ",line)
    start,end = re.split(" through ",line)
    start = [int(x) for x in re.findall("\d+",start)]
    end = [int(x) for x in re.findall("\d+",end)]
    
    for i in range(start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            if action == "turn on":
                lights[i][j] = True
            elif action == "turn off":
                lights[i][j] = False
            elif action == "toggle":
                lights[i][j] = not lights[i][j]
f.close()

count = 0
for x in lights:
    count += x.count(True)
print(count)