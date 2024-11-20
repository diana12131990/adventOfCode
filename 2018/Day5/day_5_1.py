import re

f = open("day_5_input.txt","r")

line = f.readline()
polymer = list(line)
f.close()

i = 0
while i < len(polymer)-1:
    a = polymer[i]
    b = polymer[i+1]
    if a != b and a.lower() == b.lower():
        polymer.pop(i)
        polymer.pop(i)
        i -= 1
    else:
        i += 1
        
print(len(polymer))