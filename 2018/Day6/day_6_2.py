import re

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

region_size = 0
max_total_distance = 10000

for i in range(min_x, max_x + 1):
    for j in range(min_y, max_y + 1):
        total_distance = sum(abs(x - i) + abs(y - j) for x, y in coordinates)
        if total_distance < max_total_distance:
            region_size += 1
            
print(region_size)