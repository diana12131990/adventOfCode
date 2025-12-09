
import re

f = open("day_9_input.txt","r")

red_tiles = []
for line in f:
    line = line.strip()
    x,y = line.split(",")
    red_tiles.append([int(x),int(y)])
f.close()

max_area = 0
total_red = len(red_tiles)

for i in range(total_red):
    
    x1, y1 = red_tiles[i]
    for j in range (i+1,total_red):
        
        x2, y2 = red_tiles[j]
        
        area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
        if area > max_area:
            max_area = area
            
print(max_area)