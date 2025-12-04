import re

f = open("day_4_input.txt","r")

diagram = []
total_change = 0
for line in f:
    line = line.strip()
    line = [x for x in line]
    diagram.append(line)
f.close()

row = len(diagram)
col = len(diagram[0])

for i in range(row):
    for j in range(col):
        if diagram[i][j] == "@":
            paper_count = 0
            
            for d_i in [-1, 0, 1]:
                for d_j in [-1, 0, 1]:
                    if d_i != 0 or d_j != 0:
                        n_i = i + d_i
                        n_j = j + d_j
                        if 0 <= n_i < row and 0 <= n_j < col:
                            if diagram[n_i][n_j] == "@":
                                paper_count += 1
            
            if paper_count < 4:
                total_change += 1            
                
            
print(total_change)