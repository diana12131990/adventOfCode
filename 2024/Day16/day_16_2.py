import re
from heapq import heapify, heappop, heappush

directions = [(0,1), (1,0), (0,-1), (-1,0)]

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

open_nodes = [(0, 0, start)]
heapify(open_nodes)
path = {}
cost = None

while open_nodes:
    current = heappop(open_nodes)
    cost, d, pos = current
    if (d, pos) in path:
        continue
    path[(d, pos)] = cost

    if pos == end:
        cost = (d, pos)
        break

    # move forward
    dx, dy = directions[d]
    ni, nj = pos[0] + dx, pos[1] + dy
    if maze[ni][nj] != '#':
        heappush(open_nodes, (cost + 1, d, (ni, nj)))

    # turn right
    heappush(open_nodes, (cost + 1000, (d + 1) % 4, pos))
    # turn left
    heappush(open_nodes, (cost + 1000, (d + 3) % 4, pos))


tiles = set()
stack = [(path[cost], *cost)]

while stack:
    item = stack.pop()
    cost, d, pos = item
    tiles.add(pos)

    # only add next tile if its a vald path (ie cost change is what we expect)
    def add_next(next, next_cost):
        if next in path and path[next] == next_cost:
            stack.append((next_cost, *next))

    # move backward
    reverse_dir = (d + 2) % 4
    dx, dy = directions[reverse_dir]
    ni, nj = pos[0] + dx, pos[1] + dy
    add_next((d, (ni, nj)), cost - 1)

    # turn right
    add_next(((d + 1) % 4, pos), cost - 1000)
    # turn left
    add_next(((d + 3) % 4, pos), cost - 1000)

print(len(tiles))