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

width = 101
length = 103
times = 100

for i in range(len(pos)):
    pos[i][0] += vel[i][0]*times
    pos[i][0] = pos[i][0]%width
    pos[i][1] += vel[i][1]*times
    pos[i][1] = pos[i][1]%length
    
quarter_numbers = [0]*4
for p in pos:
    if p[0] < (width-1)/2 and p[1] < (length-1)/2:
        quarter_numbers[0] += 1
    elif p[0] > (width-1)/2 and p[1] < (length-1)/2:
        quarter_numbers[1] += 1
    elif p[0] < (width-1)/2 and p[1] > (length-1)/2:
        quarter_numbers[2] += 1
    elif p[0] > (width-1)/2 and p[1] > (length-1)/2:
        quarter_numbers[3] += 1

product = reduce(operator.mul, quarter_numbers, 1)
print(product)