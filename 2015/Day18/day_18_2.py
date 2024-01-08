import re

lights = []

def AddLightOn(l):
    if l == "#":
        return 1
    else:
        return 0

def CountNeighborLight(i,j):
    count = 0
    
    if i > 0:
        count += AddLightOn(lights[i-1][j])       
        if j > 0:
            count += AddLightOn(lights[i-1][j-1])
        if j < len(lights[0])-1:
            count += AddLightOn(lights[i-1][j+1])
    
    if j > 0:
        count += AddLightOn(lights[i][j-1])
    if j < len(lights[0])-1:
        count += AddLightOn(lights[i][j+1])
        
    if i < len(lights)-1:
        count += AddLightOn(lights[i+1][j])       
        if j > 0:
            count += AddLightOn(lights[i+1][j-1])
        if j < len(lights[0])-1:
            count += AddLightOn(lights[i+1][j+1])    

    return count
    
    
f = open("day_18_input.txt","r")

for line in f:
    line = line.strip()
    
    lights.append(list(line))
f.close()

lights[0][0] = "#"
lights[0][-1] = "#"
lights[-1][0] = "#"
lights[-1][-1] = "#"

for i in range(100):
    new_lights = []
    for i in range(len(lights)):
        new_lights.append([])
        for j in range(len(lights[0])):
            if (i == 0 and j == 0) or (i == 0 and j == len(lights[0])-1) or (i == len(lights)-1 and j == 0) or (i == len(lights)-1 and j == len(lights[0])-1):
                new_lights[-1].append("#")  
            else:
                l = lights[i][j]
                neighbor_lights_count = CountNeighborLight(i, j)
                if l == "#":
                    if neighbor_lights_count == 2 or neighbor_lights_count == 3:
                        new_lights[-1].append("#")
                    else:
                        new_lights[-1].append(".")
                else:
                    if neighbor_lights_count == 3:
                        new_lights[-1].append("#")
                    else:
                        new_lights[-1].append(".")
    lights = []
    for x in new_lights:
        lights.append(x)
        
light_count = 0
for x in lights:
    light_count += x.count("#")
print(light_count)