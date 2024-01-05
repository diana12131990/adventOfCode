import re

f = open("day_3_input.txt","r")
line = f.readline()
f.close()

house_pos = [[0,0]]
si = 0
sj = 0
ri = 0
rj = 0

def Move(x,i,j):
    if x == "^":
        i -= 1
    elif x == ">":
        j += 1
    elif x == "v":
        i += 1
    elif x == "<":
        j -= 1

    return i,j

for index in range(len(line)):
    if index%2 == 0:
        si,sj = Move(line[index],si,sj)
        if [si,sj] not in house_pos:
            house_pos.append([si,sj])
    else:
        ri,rj = Move(line[index],ri,rj)
        if [ri,rj] not in house_pos:
            house_pos.append([ri,rj])
    

print(len(house_pos))