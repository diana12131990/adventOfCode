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
    step_map.append([0]*len(line))
    if not Found_guard and "^" in line:
        Found_guard = True
        i = len(guard_map)-1
        j = line.index("^")
        step_map[i][j] = 1
f.close()

block = 0
while 0 <= i+directions[d_index][0] < len(guard_map) and 0 <= j+directions[d_index][1] < len(guard_map[0]):
    while guard_map[i+directions[d_index][0]][j+directions[d_index][1]] == "#":
        d_index += 1
        if d_index == 4:
            d_index = 0
    i += directions[d_index][0]
    j += directions[d_index][1]
    print(i,j,d_index)
    previous_d = step_map[i][j]
    if previous_d != 0 and abs(previous_d-d_index) == 2:
        print("found")
        block += 1
    step_map[i][j] = d_index + 1
    
print(block)