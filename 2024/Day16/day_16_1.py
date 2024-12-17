import re

f = open("day_16_input.txt","r")

maze = []
start, end = None, None
for line in f:
    line = line.strip()
    maze.append(list(line))
    if 'S' in line:
        start = (len(maze)-1, line.index("S"))
    if 'E' in line:
        end = (len(maze)-1, line.index("E"))    
f.close()

directions = {'E': (0, 1), 'S': (1, 0), 'W': (0, -1), 'N': (-1, 0)}
directions_order = ['E', 'S', 'W', 'N']

open_nodes = [(start, 'E', 0, [start])]  # nodes are in the format (position, direction, cost, path)
visited = set()

while open_nodes:
    open_nodes.sort(key = lambda node: node[2]) # sort nodes by cost
    pos,d,cost,path = open_nodes.pop(0)
    
    if pos == end:
        print(cost)
        break

    if (pos,d) in visited:
        continue

    visited.add((pos,d)) # mark current node as visited

    for n_d in directions_order:
        n_dx, n_dy = directions[n_d]
        ni,nj = pos[0] + n_dx, pos[1] + n_dy
        if 0 <= ni < len(maze) and 0 <= nj < len(maze[0]) and maze[ni][nj] != '#':
            n_cost = cost + 1
            if n_d != d:
                n_cost += 1000
            open_nodes.append(((ni,nj), n_d, n_cost, path+[pos]))