import re

f = open("day_5_input.txt","r")

line = f.readline()
polymer = list(line)
f.close()

min_unit = -1
for c in range(ord('a'), ord('z')+1):
    remove_c = chr(c)
    current_polymer = [x for x in polymer if x.lower() != remove_c.lower()]

    i = 0
    while i < len(current_polymer)-1:
        a = current_polymer[i]
        b = current_polymer[i+1]
        if a != b and a.lower() == b.lower():
            current_polymer.pop(i)
            current_polymer.pop(i)
            i -= 1
        else:
            i += 1
    if min_unit == -1 or min_unit > len(current_polymer):
        min_unit = len(current_polymer)

print(min_unit)