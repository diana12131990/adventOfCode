import re

f = open("day_5_input.txt","r")

instruction = []
for line in f:
    line = line.strip()
    instruction.append(int(line))
f.close()

i = 0
time = 0
while i < len(instruction):
    time += 1
    step = instruction[i]
    if instruction[i] >= 3:
        instruction[i] -= 1
    else:
        instruction[i] += 1
    i += step
    
print(time)