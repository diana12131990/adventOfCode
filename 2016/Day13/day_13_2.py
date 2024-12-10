from collections import deque

favorite_num = 1364
max_steps = 50

def isOpen(x, y, fav_number):
    bin_representation = bin(x*x + 3*x + 2*x*y + y + y*y + fav_number)
    return bin_representation.count("1") % 2 == 0


queue = deque([(1, 1, 0)]) # starting position (1,1) with 0 steps
visited = set([(1,1)])
while queue:
    x, y, steps = queue.popleft() # get the next position from the queue
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]: # check all 4 adjacent positions
        nx, ny = x + dx, y + dy
        if nx >= 0 and ny >= 0 and isOpen(nx, ny, favorite_num) and (nx, ny) not in visited and steps < max_steps:
            visited.add((nx, ny))
            queue.append((nx, ny, steps + 1))


print(len(visited))