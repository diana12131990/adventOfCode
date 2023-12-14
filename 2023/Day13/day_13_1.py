import re

f = open("day_13_input.txt","r")

def DetectMirrorPos(pattern,pos):
    for line in pattern:
        for step in range(len(line)):
            if pos-step < 0 or pos+1+step >= len(line):
                break
            if line[pos - step] != line[pos+1+step]:
                return False
    return True

def DetectMirrorline(pattern,pos):
    for step in range(len(pattern)):
        if pos-step < 0 or pos+1+step >= len(pattern):
            return True
        
        if pattern[pos - step] != pattern[pos+1+step]:
            return False

def GetReflectionSum(pattern):
    Found = False
    # Find mirror pos in row
    mirror_pos = 0
    while not Found and mirror_pos <= (len(pattern) - 2):
        Found = DetectMirrorline(pattern, mirror_pos)
        if Found:
            return (mirror_pos + 1)*100
        else:
            mirror_pos += 1
            
    # Find mirror pos in colume
    mirror_pos = 0
    while not Found and mirror_pos <= (len(pattern[0]) - 2):
        Found = DetectMirrorPos(pattern, mirror_pos)
        if Found:
            return mirror_pos+1
        else:
            mirror_pos += 1

    
pattern = []
reflection_sum = 0

for line in f:
    line = line.strip()
    
    if line == "":
        reflection_sum += GetReflectionSum(pattern)
        pattern = []
    else:
        pattern.append(line)

reflection_sum += GetReflectionSum(pattern)   
print(reflection_sum)
f.close()