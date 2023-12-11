import re

f = open("day_11_input.txt","r")

def GetStarPos(pos,no_star_list):
    new_pos = pos
    for index in range(len(no_star_list)-1):
        index += 1
        if no_star_list[index-1] < pos < no_star_list[index]:
            new_pos += index*999999
            break
        elif index == len(no_star_list)-1 and pos > no_star_list[index]:
            new_pos += len(no_star_list)*999999
    return new_pos

sky_map = {}
i = 0
star_pos_x = []
star_pos_y = []
no_star_x = []
no_star_y = []

# Original Map & No star row list
for line in f:
    line = line.strip()
    line = list(line)
    sky_map.update({i:line})
    if line.count("#") == 0:
        no_star_x.append(i)
    i += 1
f.close()

# No star column list
for index in range(len(sky_map[0])):
    has_star = False
    for x in range(i):
        if sky_map[x][index] == '#':
            has_star = True
    if not has_star:
        no_star_y.append(index)

# Get each star position
for x in range(i):
    for y in range(len(sky_map[0])):
        if sky_map[x][y] == "#":
            star_pos_x.append(GetStarPos(x,no_star_x))
            star_pos_y.append(GetStarPos(y,no_star_y))

# Distance
total_distance = 0
for s1 in range(len(star_pos_x)-1):
    for s2 in range(len(star_pos_x)-s1-1):
        s2 = s2+s1+1
        distance = abs(star_pos_x[s2]-star_pos_x[s1]) + abs(star_pos_y[s2]-star_pos_y[s1])
        total_distance += distance
print(total_distance)