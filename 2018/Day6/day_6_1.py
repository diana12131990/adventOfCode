import re
from collections import defaultdict

f = open("day_6_input.txt","r")

coordinates = []
for line in f:
    pos = re.findall(r'\d+', line)
    coordinates.append((int(pos[0]),int(pos[1])))
f.close()

min_x = min(coordinates, key=lambda x: x[0])[0]
max_x = max(coordinates, key=lambda x: x[0])[0]
min_y = min(coordinates, key=lambda x: x[1])[1]
max_y = max(coordinates, key=lambda x: x[1])[1]

areas = defaultdict(int)
infinite_areas = set()

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        manhattan_dist = [abs(x - i) + abs(y - j) for x, y in coordinates]
        min_dist = min(manhattan_dist)
        if manhattan_dist.count(min_dist) == 1: 
            closest_point = manhattan_dist.index(min_dist)
            areas[closest_point] += 1

            if i == min_x or i == max_x or j == min_y or j == max_y:
                infinite_areas.add(closest_point)

finite_areas = {point: area for point, area in areas.items() if point not in infinite_areas}
print(max(finite_areas.values()))