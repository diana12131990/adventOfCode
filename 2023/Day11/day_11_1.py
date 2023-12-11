import re

f = open("day_11_input.txt","r")

sky_map = {}
i = 0
star_pos_x = []
star_pos_y = []
no_star_index = []

# Original Map & No star row list
for line in f:
    line = line.strip()
    line = list(line)
    sky_map.update({i:line})
    i += 1
    if line.count("#") == 0:
        temp_line = ["."] * len(sky_map[0])
        sky_map.update({i:temp_line})
        i += 1
f.close()

# No star column list
for index in range(len(sky_map[0])):
    has_star = False
    for x in range(i):
        if sky_map[x][index] == '#':
            has_star = True
    if not has_star:
        no_star_index.append(index)

# Get each star position
for x in range(i):
    line = sky_map[x]
    for index in range(len(no_star_index)):
        line_index = no_star_index[index] + index
        line.insert(line_index,".")
    sky_map.update({x:line})
    for y in range(len(sky_map[0])):
        if sky_map[x][y] == "#":
            star_pos_x.append(x)
            star_pos_y.append(y)

# Distance          
total_distance = 0
for s1 in range(len(star_pos_x)-1):
    for s2 in range(len(star_pos_x)-s1-1):
        s2 = s2+s1+1
        distance = abs(star_pos_x[s2]-star_pos_x[s1]) + abs(star_pos_y[s2]-star_pos_y[s1])
        total_distance += distance
print(total_distance)