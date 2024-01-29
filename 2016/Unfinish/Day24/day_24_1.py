import re
from itertools import permutations

f = open("day_24_input.txt","r")

input_map = []
numbers = []
start_i = -1
start_j = -1
for line in f:
    line = line.strip()
    if "0" in line:
        i = len(input_map)
        j = line.index("0")
        
    n = re.findall("\d+",line)
    for x in n:
        if x != "0":
            numbers.append(x)
            
    line = [x for x in line]
    input_map.append(line)
f.close()

sorted_numbers = list(permutations(numbers))

min_steps = -1
for s in sorted_numbers:
    i = start_i
    j = start_j
    total_steps = 0
    for num in s:
        building_map = []
        for line in input_map:
            building_map.append(line)   
        building_map[i][j] = "O"
        shortest_path = -1
        
        if building_map[i][j+1] == ".":
            building_map[i][j+1] = "O"
            FindSteps(i,j+1,">",1,num)
            building_map[i][j+1] = "."
            
        if building_map[i+1][j] == ".":
            building_map[i+1][j] = "O"
            FindSteps(i+1,j,"v",1,num)
            building_map[i+1][j] = "."
            
        if building_map[i][j-1] == ".":
            building_map[i][j-1] = "O"
            FindSteps(i,j-1,"<",1,num)
            building_map[i][j-1] = "."
            
        if building_map[i+1][j] == ".":
            building_map[i+1][j] = "O"
            FindSteps(i+1,j,"^",1,num)
            building_map[i+1][j] = "."   
        
        total+= shortest_path