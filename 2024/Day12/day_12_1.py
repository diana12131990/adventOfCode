import re

f = open("day_12_input.txt","r")

garden = []
regions_check = []
for line in f:
    line = line.strip()
    garden.append(list(line))
    regions_check.append([False]*len(line))
f.close()

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
region_info = []
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if not regions_check[i][j]:
            plant = garden[i][j]
            area = 0
            perimeter = 0
            check_pos = [(i, j)]
            while check_pos:
                x, y = check_pos.pop()
                if not regions_check[x][y]:
                    regions_check[x][y] = True
                    area += 1
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if (not (0 <= nx < len(garden) and 0 <= ny < len(garden[0]))) or garden[nx][ny] != plant:
                            perimeter += 1
                        else:
                            check_pos.append((nx, ny))            
            region_info.append({'plant': plant, 'area': area, 'perimeter': perimeter})

total_cost = sum(info['area']*info['perimeter'] for info in region_info)

print(total_cost)