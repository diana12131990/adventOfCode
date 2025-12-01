import re

f = open("day_1_input.txt","r")

num = 50
zero_count = 0
previous_zero = False
for line in f:
    direction = line[0]
    steps = int(line[1:].strip())
    #print(direction, steps)
    
    if steps > 99:
        zero_count += int(steps/100)
        steps %= 100
        if steps == 0:
            zero_count -= 1
        #print(zero_count)
    if direction == "L":
        steps *= -1
    
    num += steps
    if num < 0:
        num += 100
        if not previous_zero and num != 0:
            zero_count += 1
            #print(zero_count)
    elif num > 99:
        num -= 100
        if not previous_zero and num != 0:
            zero_count += 1
            #print(zero_count)
    
    if num == 0:
        previous_zero = True
        zero_count += 1
        #print(zero_count)
    elif num != 0 and previous_zero:
        previous_zero = False
f.close()


print(zero_count)