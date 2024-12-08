import re

f = open("day_6_input.txt","r")

guard_map = []
step_map = []
Found_guard = False
i = 0
j = 0
d = (-1,0)
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


while 0 <= i+d[0] < len(guard_map) and 0 <= j+d[1] < len(guard_map[0]):
    while guard_map[i+d[0]][j+d[1]] == "#":
        if d == (-1,0):
            d = (0,1)
        elif d == (0,1):
            d = (1,0)
        elif d == (1,0):
            d = (0,-1)
        elif d == (0,-1):
            d = (-1,0)
    i += d[0]
    j += d[1]
    step_map[i][j] = 1
    
print(sum(row.count(1) for row in step_map))