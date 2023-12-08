import re
import fractions

f = open("day_8_input.txt","r")

map_network = {}
instruction = []
c_pos = []
all_step = []
        
line = f.readline()
line = line.strip()
for x in line:
    if x == "L":
        instruction.append(0)
    elif x == "R":
        instruction.append(1)

f.readline()    #skip empty line

for line in f:
    line = line.strip()
    pos, side = re.split(" = ",line)
    if pos[-1] == "A":
        c_pos.append(pos)
    left, right = re.split(", ",side)
    left = left.replace("(","")
    right = right.replace(")","")
    map_network.update({pos:[left,right]})
f.close()

for pos in c_pos:
    index = 0
    step = 0
    while pos[-1] != "Z":
        c_dir = instruction[index]
        pos = map_network[pos][c_dir]
        step += 1
        
        index += 1
        if index == len(instruction):
            index = 0
            
    all_step.append(step)

# I don't have math.lcm() in old python version so I use fractions.gcd() instead    
step = all_step[0]
for i in all_step[1:]:
    step = (step * i) // fractions.gcd (step, i)

print(step)