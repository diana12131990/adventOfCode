import re

f = open("day_2_input.txt","r")

i = 1
j = 1
code = 0

for line in f:
    line = line.strip()
    for x in line:
        if x == "U" and i > 0:
            i -= 1
        elif x == "L" and j > 0:
            j -= 1
        elif x == "D" and i < 2:
            i += 1
        elif x == "R" and j < 2:
            j += 1
    
    digit = 3*i+j+1
    code *= 10
    code += digit
f.close()

print(code)