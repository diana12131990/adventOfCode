import re

f = open("day_6_input.txt","r")

guard_map = []
step_map = []
Found_guard = False
i = 0
j = 0
directions = [(-1,0),(0,1),(1,0),(0,-1)]
d_index = 0
for line in f:
    line = line.strip()
    line = [x for x in line]
    guard_map.append(line)
    step_map.append([[] for _ in range(len(line))])
    if not Found_guard and "^" in line:
        Found_guard = True
        i = len(guard_map)-1
        j = line.index("^")
        step_map[i][j].append(1)
    for line_i in range(len(line)):
        if line[line_i] == "#":
            step_map[len(guard_map)-1][line_i].append(9)
f.close()

def FindLoop(d_index,i,j):
    x = i
    y = j
    if d_index == 0:     #up -> check right
        while y < len(step_map[0]):
            if 9 in step_map[x][y]:
                return False
            elif 2 in step_map[x][y]:
                return True
            else:
                y += 1   
    elif d_index == 1:  #right -> check down
        while x < len(step_map):
            if 9 in step_map[x][y]:
                return False
            elif 3 in step_map[x][y]:
                return True
            else:
                x += 1
    
    elif d_index == 2:   #down -> check left
        while y >= 0:
            if 9 in step_map[x][y]:
                return False
            elif 4 in step_map[x][y]:
                return True
            else:
                y -= 1   
    else:                #left -> check up
        while x >= 0:
            if 9 in step_map[x][y]:
                return False
            elif 1 in step_map[x][y]:
                return True
            else:
                x -= 1    
    return False    
            

block = 0
while 0 <= i+directions[d_index][0] < len(guard_map) and 0 <= j+directions[d_index][1] < len(guard_map[0]):
    while guard_map[i+directions[d_index][0]][j+directions[d_index][1]] == "#":
        d_index += 1
        if d_index == 4:
            d_index = 0
    i += directions[d_index][0]
    j += directions[d_index][1]
    if FindLoop(d_index,i,j):
        block += 1
    if d_index+1 not in step_map[i][j]:
        step_map[i][j].append(d_index + 1)
    
print(block)