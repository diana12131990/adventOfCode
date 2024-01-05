import re

f = open("day_5_input.txt","r")

def HasDoubleDouble(line):
    for i in range(len(line)-3):
        string = line[i:i+2]
        if string in line[i+2:]:
            return True
    return False

def HasSandwich(line):
    for i in range(1,len(line) - 1):
        if line [i-1] == line[i+1]:
            return True
    return False

nice = 0
for line in f:
    line = line.strip()
    if HasDoubleDouble(line) and HasSandwich(line):
        nice += 1
        
f.close()

print(nice)