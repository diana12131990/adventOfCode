import re
from heapq import heapify, heappop, heappush

directions = [(0,1), (1,0), (0,-1), (-1,0)]
cheat_time = 20

f = open("day_20_input.txt","r")

racetrack = []
start, end = None, None
for line in f:
    line = line.strip()
    racetrack.append(list(line))
    if 'S' in line:
        start = (len(racetrack)-1, line.index("S"))
    if 'E' in line:
        end = (len(racetrack)-1, line.index("E"))    
f.close()

open_nodes = [(0, [], start)]
heapify(open_nodes)
cheat = {}
best_path = []

while open_nodes:
    current = heappop(open_nodes)
    d, path, pos = current
    if pos in cheat:
        continue

    cheat[pos] = d
    path = path + [pos]

    if pos == end:
        best_path = path
        break

    for dx, dy in directions:
        ni, nj = pos[0] + dx, pos[1] + dy
        if racetrack[ni][nj] != '#':
            heappush(open_nodes, (d + 1, path, (ni, nj)))


result = 0
for start_pos in best_path:
    for i in range(-cheat_time, cheat_time + 1):
        for j in range(-cheat_time, cheat_time + 1):
            time = abs(i) + abs(j)
            if time <= cheat_time:
                pos = (start_pos[0] + i, start_pos[1] + j)
                if pos in cheat:
                    cheat_save = cheat[pos] - (cheat[start_pos] + time)
                    if cheat_save >= 100:
                        result += 1

print(result)