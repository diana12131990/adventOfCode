import re

f = open("day_3_input.txt","r")
line = f.readline()
f.close()

house_pos = [[0,0]]
i = 0
j = 0

for x in line:
    if x == "^":
        i -= 1
    elif x == ">":
        j += 1
    elif x == "v":
        i += 1
    elif x == "<":
        j -= 1
    
    if [i,j] not in house_pos:
        house_pos.append([i,j])
    

print(len(house_pos))