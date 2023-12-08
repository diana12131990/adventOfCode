import re

f = open("day_8_input.txt","r")

map_network = {}
instruction = []
c_pos = "AAA"
step = 0
        
line = f.readline()
line = line.strip()
for x in line:
    if x == "L":
        instruction.append(0)
    elif x == "R":
        instruction.append(1)
index = 0

f.readline()

for line in f:
    line = line.strip()
    pos, side = re.split(" = ",line)
    left, right = re.split(", ",side)
    left = left.replace("(","")
    right = right.replace(")","")
    map_network.update({pos:[left,right]})
f.close()

while c_pos != "ZZZ":
    c_dir = instruction[index]
    c_pos = map_network[c_pos][c_dir]
    step += 1
    
    index += 1
    if index == len(instruction):
        index = 0

print(step)