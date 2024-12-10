import re

f = open("day_10_input.txt","r")

topo_map = []
for line in f:
    line = line.strip()
    line = list(line)
    topo_map.append(line)
f.close()

directions = [(-1,0) , (0,1) , (1,0) , (0,-1)]       # up, right, down, left
trails = {}
    
def FindTrail(x, y, trailhead):
    if topo_map[x][y] == '9':
        trails[trailhead].append((x,y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(topo_map) and 0 <= ny < len(topo_map[0]) and topo_map[nx][ny] != '.':
            if int(topo_map[nx][ny]) - int(topo_map[x][y]) == 1:
                FindTrail(nx, ny, trailhead)
        
for i in range(len(topo_map)):
    for j in range(len(topo_map[0])):
        if topo_map[i][j] == '0':
            trails[(i,j)] = []
            FindTrail(i,j,(i,j))

score = 0
for trailhead in trails:
    score += len(trails[trailhead])
print(score)