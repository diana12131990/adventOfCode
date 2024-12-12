import re

f = open("day_12_input.txt","r")

garden = []
regions_check = []
for line in f:
    line = line.strip()
    garden.append(list(line))
    regions_check.append([False]*len(line))
f.close()

def GetPlant(x, y, garden, area):
    plant = None
    if 0 <= x < len(garden) and 0 <= y < len(garden[0]):
        if (x, y) in area:
            plant = garden[x][y]
    return plant

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
diagonals = [(1,1),(-1,-1),(1,-1),(-1,1)]
region_info = []
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if not regions_check[i][j]:
            plant = garden[i][j]
            start = (i, j)
            area = set()
            area.add(start)
            check_pos = [(i, j)]
            while check_pos:
                x, y = check_pos.pop()
                if not regions_check[x][y]:
                    regions_check[x][y] = True
                    area.add((x,y))
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if not ((not (0 <= nx < len(garden) and 0 <= ny < len(garden[0]))) or garden[nx][ny] != plant):
                            check_pos.append((nx, ny))

            sides = 0
            for pos in area:
                num_neighbours = 0
                x, y = pos
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in area:
                        num_neighbours += 1       
                        
                # Single plant -> 4 sides
                if num_neighbours == 0:
                    sides += 4
                # a tip of a row -> 2 sides
                elif num_neighbours == 1:
                    sides += 2
                else: # Has at least 2 neighbour in the same area. 
                    # detect if pos is at corner
                    x, y = pos
                    plant = garden[x][y]
                    for dx, dy in diagonals:
                        nx, ny = x + dx, y + dy
        
                        diagonal_plant = GetPlant(nx, ny, garden, area)
                        p1 = GetPlant(nx, y, garden, area)
                        p2 = GetPlant(x, ny, garden, area)
        
                        # If plant on diagonal position is different, either inside or outside corner
                        if (diagonal_plant != plant and p1 == plant and p2 == plant) or (p1 != plant and p2 != plant):
                            sides += 1               
            region_info.append({'plant': plant, 'area': len(area), 'sides': sides})            


total_cost = sum(info['area']*info['sides'] for info in region_info)
print(total_cost)