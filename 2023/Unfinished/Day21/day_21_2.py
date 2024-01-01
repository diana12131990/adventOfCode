import re

f = open("day_21_input.txt","r")

garden = []

for line in f:
    line = line.strip()
    garden.append(list(line))
f.close()

def GetStep(i,j,step_map):
    # north
    if i == 0:
        n = len(garden)-1
        if garden[n][j] != "#":
            step_map[n][j] += 1        
    else:
        n = i-1
        if garden[n][j] != "#" and step_map[n][j] == 0:
            step_map[n][j] = 1
        
    # south
    if (i+1) == len(garden):
        n = 0
        if garden[n][j] != "#":
            step_map[n][j] += 1        
    else:
        n = i+1
        if garden[n][j] != "#" and step_map[n][j] == 0:
            step_map[n][j] = 1        

    # west
    if j == 0:
        n = len(garden[0])-1
        if garden[i][n] != "#":
            step_map[i][n] += 1        
    else:
        n = j-1
        if garden[i][n] != "#" and step_map[i][n] == 0:
            step_map[i][n] = 1            
        
    # east
    if (j+1) == len(garden[0]):
        n = 0
        if garden[i][n] != "#":
            step_map[i][n] += 1        
    else:
        n = j+1
        if garden[i][n] != "#" and step_map[i][n] == 0:
            step_map[i][n] = 1        

    return step_map

step_map = []
last_map = []
for step in range(10):
    last_map = step_map
    step_map = []
    for i in range(len(garden)):
        step_map.append([0]*len(garden[0]))
    if last_map == []:
        for index in range(len(garden)):
            if "S" in garden[index]:
                i = index
                j = garden[i].index("S")
                step_map = GetStep(i,j,step_map)
                break  
    else:
        for i in range(len(last_map)):
            for j in range(len(last_map[i])):
                if last_map[i][j] > 0:
                    step_map = GetStep(i,j,step_map)
    for x in step_map:
        print(x)
    print("\n\n\n")
total_step = 0
for x in step_map:
    total_step += sum(x)
print(total_step)