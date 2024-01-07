import re

f = open("day_8_input.txt","r")

total_count = 0
for line in f:
    line = line.strip()
    line_count = len(line)
    line = line[1:len(line)-1]
    chr_count = 0
    while line != "":
        if line[0] == "\\":
            if line[1] == "\"" or line[1] == "\\":
                line = line[2:]
            elif line[1] == "x":
                line = line[4:]
        else:
            line = line[1:]
        chr_count += 1
            
    total_count += line_count - chr_count
f.close()

print(total_count)