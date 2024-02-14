import re

f = open("day_4_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    values = line.split()
    
    values_list = []
    for x in values:
        chars = list(x)
        chars.sort()
        values_list.append(chars)
    
    Invaild = False
    for x in values_list:
        if values_list.count(x) > 1:
            Invaild = True
            break
    if not Invaild:
        total += 1
    
print(total)
f.close()