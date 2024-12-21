import re

f = open("day_20_input.txt","r")

racetrack = []
start, end, pos = None, None, None
for line in f:
    line = line.strip()
    racetrack.append(list(line))
    if 'S' in line:
        start = (len(racetrack)-1, line.index("S"))
        pos = start
    if 'E' in line:
        end = (len(racetrack)-1, line.index("E"))    
f.close()

directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}

path_info = []
path_pos = []
visited = set()
while pos != end:
    visited.add(pos)
    for d in directions.keys():
        dx, dy = directions[d]
        ni,nj = pos[0] + dx, pos[1] + dy
        if 1 <= ni < len(racetrack)-1 and 1 <= nj < len(racetrack[0])-1 and (ni,nj) not in visited and racetrack[ni][nj] != '#':
            path_info.append((pos, d))
            path_pos.append((pos))
            pos = (ni,nj)
            break
path_pos.append(end)
    
visited = set()
cheat = {}
for i in range(len(path_info)):
    pos, d = path_info[i]
    visited.add(pos)
    for nd in directions.keys():
        if nd == d:
            continue
        dx, dy = directions[nd]
        ni, nj = pos[0]+dx, pos[1]+dy
        if racetrack[ni][nj] != '#' or (ni,nj) in visited:
            continue
        ni, nj = pos[0]+dx*2, pos[1]+dy*2
        if 1 <= ni < len(racetrack)-1 and 1 <= nj < len(racetrack[0])-1 and (ni,nj) not in visited and (ni,nj) in path_pos:
            j = path_pos.index((ni,nj))
            save = j-i-2
            if save in cheat:
                cheat[save] += 1
            else:
                cheat.update({save:1})
                
result = 0
for x in cheat.keys():
    if x >= 100:
        result += cheat[x]
print(result)