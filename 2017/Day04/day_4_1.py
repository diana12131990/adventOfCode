import re

f = open("day_4_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    values = line.split()
    
    Invaild = False
    for x in values:
        if values.count(x) > 1:
            Invaild = True
            break
    if not Invaild:
        total += 1
    
print(total)
f.close()