from collections import deque
from itertools import permutations



def bfs(start, end, maze):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        (x, y), cnt = queue.popleft()

        if (x, y) in visited:
            continue

        if (x, y) == end:
            return cnt

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x, next_y = x + dx, y + dy

            if next_y < 0 or next_y >= len(maze) or next_x < 0 or next_x >= len(maze[0]):
                continue

            if maze[next_y][next_x] == '.' or maze[next_y][next_x].isdigit():
                queue.append(((next_x, next_y), cnt + 1))

    raise ValueError('No Path found')



f = open('day_24_input.txt', 'r')

maze = []
for line in f:
    line = line.strip()
    maze.append(list(line))
f.close()

points = {}
for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x].isdigit():
            points[maze[y][x]] = (x, y)

distances = {}
for k1, p1 in points.items():
    for k2, p2 in points.items():
        if k1 == k2:
            continue
        if (k1, k2) not in distances:
            distance = bfs(p1, p2, maze)
            distances[(k1, k2)] = distance
            distances[(k2, k1)] = distance

min_len = float('inf')
points_keys = list(points.keys())
points_keys.remove('0')

for perm in permutations(points_keys):
    path = ['0'] + list(perm) + ['0'] # Added '0' at the end for the return trip
    total_distance = sum([distances[(path[i], path[i+1])] for i in range(len(path)-1)])
    min_len = min(min_len, total_distance)

print(min_len)