import re

f = open("day_21_input.txt","r")

garden = []

for line in f:
    line = line.strip()
    garden.append(list(line))
f.close()

def GetStep(i,j,step_map):
    if i != 0:
        if garden[i-1][j] != "#":
            step_map[i-1][j] = "O"
    # south
    if (i+1) != len(garden):
        if garden[i+1][j] != "#":
            step_map[i+1][j] = "O"
    # west
    if j != 0:
        if garden[i][j-1] != "#":
            step_map[i][j-1] = "O"
    # east
    if (j+1) != len(garden[0]):
        if garden[i][j+1] != "#":
            step_map[i][j+1] = "O"    
    return step_map

step_map = []
last_map = []
for step in range(64):
    last_map = step_map
    step_map = []
    for i in range(len(garden)):
        step_map.append(list("."*len(garden[0])))
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
                if last_map[i][j] == "O":
                    step_map = GetStep(i,j,step_map)
total_step = 0
for x in step_map:
    total_step += x.count("O")
print(total_step)