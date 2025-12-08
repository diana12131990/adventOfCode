
import re

f = open("day_7_input.txt","r")

# Get first line info
line = f.readline().strip()
branch_check_index = {line.find("S")}
split_amount = 0

# Do the rest
for line in f:
    line = line.strip()
    
    current_branch = branch_check_index
    branch_check_index = set()
    
    for i in current_branch:
        if line[i] == "^":
            split_amount += 1
            if i-1 >= 0:
                branch_check_index.add(i-1)
            if i+1 < len(line):
                branch_check_index.add(i+1)
        else:
            branch_check_index.add(i)
f.close()

print(split_amount)