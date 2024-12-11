
bursts = 10000
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
dir = 0  # start facing Up

with open('day_22_input.txt', 'r') as f:
    map = [list(line.strip()) for line in f.readlines()]

size = len(map)
mid = size // 2  # the original center

infected = {(i-mid, j-mid): True for i in range(size) for j in range(size) if map[i][j] == '#'}
infections = 0
carrier_x, carrier_y = 0, 0  # start in the middle - which is the origin (0,0)

for _ in range(bursts):
    if (carrier_x, carrier_y) in infected:
        # Infected
        del infected[(carrier_x, carrier_y)]  # Clean
        dir = (dir + 1) % 4  # Turn right
    else:
        # Clean
        infected[(carrier_x, carrier_y)] = True  # Infects
        infections += 1
        dir = (dir - 1) % 4  # Turn left
        
    dx, dy = dirs[dir]
    carrier_x += dx
    carrier_y += dy


print(infections)