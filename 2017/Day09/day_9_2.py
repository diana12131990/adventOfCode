import re

f = open("day_9_input.txt","r")

line = f.readline()
line = line.strip()
f.close()

inGarbage = False
isIgnore = False
garbage_amount = 0

for x in line:
    if isIgnore:
        isIgnore = False
    else:
        if inGarbage:
            if x == "!":
                isIgnore = True
            elif x == ">":
                inGarbage = False
            else:
                garbage_amount += 1            
        else:
            if x == "<":
                inGarbage = True

print(garbage_amount)