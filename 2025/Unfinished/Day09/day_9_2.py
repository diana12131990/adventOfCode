
import re
import sys

f = open("day_9_input.txt","r")

red_tiles = []
border = set()
for line in f:
    line = line.strip()
    x,y = line.split(",")
    red_tiles.append((int(x),int(y)))
f.close()

min_x = min(t[0] for t in red_tiles)
max_x = max(t[0] for t in red_tiles)
min_y = min(t[1] for t in red_tiles)
max_y = max(t[1] for t in red_tiles)
total_red = len(red_tiles)
vaild_tiles = set(red_tiles)

# Get green tiles first (check the border)
for i in range(total_red):
    x1, y1 = red_tiles[i]
    x2, y2 = red_tiles[(i+1) % total_red]
    
    if x1 == x2:
        for y in range(min(y1,y2)+1, max(y1,y2)):
            vaild_tiles.add((x1,y))
    elif y1 == y2:
        for x in range(min(x1,x2)+1, max(x1,x2)):
            vaild_tiles.add((x,y1))
            
# Get all the vaild tiles inside the border
for y in range(min_y,max_y+1):
    boundary_x_at_y = sorted(list(set(edge_x for edge_x,edge_y in vaild_tiles if edge_y == y)))
    for x in range(boundary_x_at_y[0],boundary_x_at_y[-1]):
        if (x,y) not in vaild_tiles:
            intersections = 0
            
            for i in range(total_red):
                x1, y1 = red_tiles[i]
                x2, y2 = red_tiles[(i+1) % total_red]
                if x1 == x2 and x1 > x and min(y1,y2) <= y < max(y1,y2):
                    intersections += 1
                    
            if intersections %2 == 1:
                vaild_tiles.add((x,y))
                
   
max_area = 0
for i in range(total_red):
    
    x1, y1 = red_tiles[i]
    for j in range (i+1,total_red):
        
        x2, y2 = red_tiles[j]
        
        if (x1,y2) in vaild_tiles and (x2,y1) in vaild_tiles:
            area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
            if area > max_area:
                max_area = area
            
print(max_area)