import re

f = open("day_1_input.txt","r")

line = f.readline()
f.close()

floor = 0
for i in range(len(line)):
    if line[i] == "(":
        floor += 1
    elif line[i] == ")":
        floor -= 1
        if floor < 0:
            print(i+1)
            break
