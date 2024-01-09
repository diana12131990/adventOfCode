import re
from itertools import groupby

f = open("day_6_input.txt","r")

lines = [[],[],[],[],[],[],[],[]]
for line in f:
    line = line.strip()
    for i in range(8):
        lines[i].append(line[i])
f.close()

message = ""
for x in lines:
    x.sort()
    
    max_amount = 0
    max_key = ""
    for key, group in groupby("".join(x)):
        amount = len(list(group))
        if amount > max_amount:
            max_amount = amount
            max_key = key
            
    message += max_key
print(message)