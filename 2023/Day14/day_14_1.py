import re

f = open("day_14_input.txt","r")

mirror = []
load_sum = 0

for line in f:
    line = line.strip()
    line = [x for x in line]
    if mirror != []:
        for i in range(len(line)):
            if line[i] == "O":
                row = len(mirror) - 1
                while row >= 0:
                    if mirror[row][i] == "O" or mirror[row][i] == "#":
                        row += 1
                        break
                    else:
                        if row == 0:
                            break
                        row -= 1
                if row != len(mirror):
                    mirror[row][i] = "O"
                    line[i] = "."
    mirror.append(line)

for i in range(len(mirror)):
    load_amount = len(mirror) - i
    total_rock = mirror[i].count("O")
    load_sum += load_amount * total_rock

print(load_sum)
   
f.close()