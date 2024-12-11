def knot_hash(input):
    lengths = [ord(ch) for ch in input] + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    position = 0
    skip_size = 0
    for _ in range(64):
        for length in lengths:
            if length > 1:
                numbers = numbers[position:] + numbers[:position]
                numbers[:length] = reversed(numbers[:length])
                numbers = numbers[-position:] + numbers[:-position]
            position = (position + length + skip_size) % 256
            skip_size += 1
    dense = [0]*16
    for i in range(16):
        for j in range(16):
            dense[i] ^= numbers[i*16+j]
    return "".join(f"{i:02x}" for i in dense)

def mark_region(x, y, grid):
    dxy = [(0,1), (0,-1), (1,0), (-1,0)]
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if grid[x][y] == '1':
            grid[x][y] = '0'
            for dx, dy in dxy:
                nx, ny = x+dx, y+dy
                if 0<=nx<128 and 0<=ny<128 and grid[nx][ny] =='1':
                    stack.append((nx, ny))
                    
key_str = "hxtvlmkl"

grid = []
for i in range(128):
    s = f"{key_str}-{i}"
    knot_hash_string = knot_hash(s)
    binary_hash = bin(int(knot_hash_string, 16))[2:].zfill(128)
    grid.append(list(binary_hash))
    
n_regions = 0
for i in range(128):
    for j in range(128):
        if grid[i][j] == '1':
            mark_region(i, j, grid)
            n_regions += 1
print(n_regions)