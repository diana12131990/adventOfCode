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
    
    min_amount = -1
    min_key = ""
    for key, group in groupby("".join(x)):
        amount = len(list(group))
        if min_amount == -1 or amount < min_amount:
            min_amount = amount
            min_key = key
            
    message += min_key
print(message)