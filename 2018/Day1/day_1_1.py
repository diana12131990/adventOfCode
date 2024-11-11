import re
f = open("day_1_input.txt","r")

total = 0
for line in f:
    total += int(line)

print(total)
f.close()