import re

f = open("day_8_input.txt","r")

frequency_dict = {}
antinode_map = []
i = 0
for line in f:
    line = line.strip()
    antinode_map.append(["."]*len(line))
    for j in range(len(line)):
        if line[j] != ".":
            char = line[j]
            if char in frequency_dict:
                frequency_dict[char].append((i, j))
            else:
                frequency_dict[char] = [(i, j)]
    i += 1
f.close()

for char in frequency_dict:
    positions = frequency_dict[char]
    for x in range(len(positions)-1):
        for y in range(x+1,len(positions)):
            d_i = positions[y][0] - positions[x][0]
            d_j = positions[y][1] - positions[x][1]
            
            p1_x = positions[x][0] - d_i
            p1_y = positions[x][1] - d_j
            
            if 0 <= p1_x < len(antinode_map) and 0 <= p1_y < len(antinode_map[0]):
                antinode_map[p1_x][p1_y] = "#"
            
            p2_x = positions[y][0] + d_i
            p2_y = positions[y][1] + d_j
            
            if 0 <= p2_x < len(antinode_map) and 0 <= p2_y < len(antinode_map[0]):
                antinode_map[p2_x][p2_y] = "#"

count = 0
for line in antinode_map:
    count += line.count("#")
print(count)