import re
import copy

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


def Turn(old_d):
    if old_d == (-1,0):
        return (0,1)
    elif old_d == (0,1):
        return (1,0)
    elif old_d == (1,0):
        return (0,-1)
    else:
        return (-1,0)

def IsInLoop(g_map,s_map,ti,tj,td):
    while 0 <= ti+td[0] < len(g_map) and 0 <= tj+td[1] < len(g_map[0]):
        while g_map[ti+td[0]][tj+td[1]] == "#":
            td = Turn(td)
        ti += td[0]
        tj += td[1]
        s_map[ti][tj] += 1
        if s_map[ti][tj] == 5:
            return True
    return False

blocks = []
start_pos = (i,j)
while 0 <= i+d[0] < len(guard_map) and 0 <= j+d[1] < len(guard_map[0]):
    while guard_map[i+d[0]][j+d[1]] == "#":
        d = Turn(d)
    i += d[0]
    j += d[1]
    if step_map[i][j] != 1 and (i,j) not in blocks and (i,j) != start_pos:
        original_node = guard_map[i][j]
        guard_map[i][j] = "#"
        temp_step_map = copy.deepcopy(step_map)
        test_d = d
        if IsInLoop(guard_map,temp_step_map,i-d[0],j-d[1],test_d):
            blocks.append((i,j))
        guard_map[i][j] = original_node
        step_map[i][j] = 1
    
print(len(blocks))