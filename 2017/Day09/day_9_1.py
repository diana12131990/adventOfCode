import re

f = open("day_9_input.txt","r")

line = f.readline()
line = line.strip()
f.close()

score = 0
layer = 1
inGarbage = False
isIgnore = False

for x in line:
    if isIgnore:
        isIgnore = False
    else:
        if x == "<":
            inGarbage = True
        elif x == ">":
            inGarbage = False
        elif x == "!" and inGarbage:
            isIgnore = True
        elif not inGarbage:
            if x == "{":
                score += layer
                layer += 1
            elif x == "}":
                layer -= 1
print(score)