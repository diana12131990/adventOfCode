import re

f = open("day_18_input.txt","r")

safe_count = 0
line = f.readline()
line = [x for x in line]
safe_count += line.count(".")
f.close()

def IsTrap(left,center,right):
    if left != right:
        return True
    else:
        return False

column_length = len(line)
for t in range(400000-1):
    new_line = []
    for i in range(column_length):
        if i == 0:
            FoundTrap = IsTrap(".",line[i],line[i+1])
        elif i == column_length - 1:
            FoundTrap = IsTrap(line[i-1],line[i],".")
        else:
            FoundTrap = IsTrap(line[i-1],line[i],line[i+1])
        
        if FoundTrap:
            new_line.append("^")
        else:
            new_line.append(".")
            
    safe_count += new_line.count(".")
    line = new_line
print(safe_count)