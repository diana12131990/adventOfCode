import re

f = open("day_8_input.txt","r")

total_count = 0
for line in f:
    line = line.strip()
    before_line_count = len(line)
    after_line_count = 1
    while line != "":
        if line[0] == "\"" or line[0] == "\\":
            after_line_count += 2
        else:
            after_line_count += 1
        line = line[1:]
    after_line_count += 1
    total_count += after_line_count - before_line_count
f.close()

print(total_count)