import re

f = open("day_1_input.txt","r")

num = 50
zero_count = 0
for line in f:
    direction = line[0]
    steps = int(line[1:].strip())
    #print(direction, steps)
    
    if steps > 99:
        steps %= 100
        #print(steps)
    if direction == "L":
        steps *= -1
    
    num += steps
    if num < 0:
        num += 100
    elif num > 99:
        num -= 100
    #print(num)
    
    if num == 0:
        zero_count += 1
f.close()


print(zero_count)