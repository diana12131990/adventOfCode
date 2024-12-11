def read_map(file_name):
    with open(file_name, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def process_map(file_name, bursts):
    # Directions: Up, Right, Down, Left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir = 0  # start facing Up

    map = read_map(file_name)
    size = len(map)
    mid = size // 2  # the original center
    
    states = {(i-mid, j-mid): 'I' for i in range(size) for j in range(size) if map[i][j] == '#'}
    infections = 0
    carrier_x, carrier_y = 0, 0  # start in the middle - which is the origin (0, 0)

    for _ in range(bursts):
        state = states.get((carrier_x, carrier_y), 'C')  # Clean by default
        if state == 'C':
            dir = (dir - 1) % 4  # Turn left
            states[(carrier_x, carrier_y)] = 'W'  # Weaken
        elif state == 'W':
            infections += 1
            states[(carrier_x, carrier_y)] = 'I'  # Infect
        elif state == 'I':
            dir = (dir + 1) % 4  # Turn right
            states[(carrier_x, carrier_y)] = 'F'  # Flag
        elif state == 'F':
            dir = (dir + 2) % 4  # Reverse
            states[(carrier_x, carrier_y)] = 'C'  # Clean
            
        dx, dy = dirs[dir]
        carrier_x += dx
        carrier_y += dy

    return infections

print(process_map('day_22_input.txt', 10000000))