import re

start = (0, 0)
end = (70, 70)

corrupted_bytes = []
grid = [['.' for _ in range(71)] for _ in range(71)]
f = open("day_18_input.txt", "r")

for line in f:
    pos = re.findall(r'\d+',line)
    x,y = int(pos[0]),int(pos[1])
    corrupted_bytes.append((x, y))
f.close()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i, (x, y) in enumerate(corrupted_bytes):
    grid[x][y] = '#'

    Found = False
    queue = [start]
    visited = set([start])
    path_length = 0
    shortest_path = -1
    
    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            # Check if we have reached the end
            if x == end[0] and y == end[1]:
                shortest_path = path_length
                Found = True
                break
            # Explore the neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[nx][ny] != '#':
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        path_length += 1
        if Found:
            break
    
    if not Found:
        print(corrupted_bytes[i])
        break