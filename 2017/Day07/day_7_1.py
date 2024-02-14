import re

f = open("day_7_input.txt","r")

instruction = []
for line in f:
    line = line.strip()
    if "->" in line:
        front, back = re.split(" -> ",line)
        parent,_ = re.split(" ",front)
        children = back.split(", ")
        instruction.append([parent,children])
f.close()

# Find root
start_index = -1
for i in range(len(instruction)):
    name = instruction[i][0]
    Skip = False
    for j in range(len(instruction)):
        if j != i:
            if name in instruction[j][1]:
                Skip = True
                break
    if not Skip:
        start_index = i
        break

name = instruction[start_index][0]

print(name)