import re

f = open("day_15_input.txt","r")

box_map = []
direction = ""
map_done = False
i = 0
j = 0
for line in f:
    line = line.strip()
    if line == "":
        map_done = True
    else:
        if not map_done:
            box_map.append(list(line))
            if "@" in line:
                i = len(box_map)-1
                j = line.index("@")
        else:
            direction += line
f.close()

direction = list(direction)

def Detect(i,j,d):
    x,y = d
    box_num = 0
    if box_map[i+x][j+y] != "#":
        check_i,check_j = i+x, j+y
        while box_map[check_i][check_j] == "O":
            box_num += 1
            check_i += x
            check_j += y
        if box_map[check_i][check_j] != "#":
            if box_num != 0:
                box_map[check_i][check_j] = "O"
            box_map[i+x][j+y] = "@"
            box_map[i][j] = "."
            return True
    return False

for d in direction:
    if d == "<" and Detect(i,j,(0,-1)):
        j -= 1
    elif d == "^" and Detect(i,j,(-1,0)):
        i -= 1
    elif d == ">" and Detect(i,j,(0,1)):
        j += 1
    elif d == "v" and Detect(i,j,(1,0)):
        i += 1
        
result = 0
for x in range(len(box_map)):
    line = box_map[x]
    if "O" in line:
        indices = [y for y, char in enumerate(line) if char == "O"]
        for y in indices:
            result += 100*x+y
print(result)