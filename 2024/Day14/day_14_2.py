import re
from functools import reduce
import operator

f = open("day_14_input.txt","r")

pos = []
vel = []
for line in f:
    numbers = re.findall(r'-?\d+\.?\d*', line)
    pos.append([int(numbers[0]),int(numbers[1])])
    vel.append([int(numbers[2]),int(numbers[3])])
f.close()

time = 0
while True:
    time += 1
    for i in range(len(pos)):
        pos[i][0] += vel[i][0]
        pos[i][0] = pos[i][0] % 101
        pos[i][1] += vel[i][1]
        pos[i][1] = pos[i][1] % 103
        
    
    coords = set((x,y) for x,y in pos)
    if len(coords) == len(pos):
        break
print(time)