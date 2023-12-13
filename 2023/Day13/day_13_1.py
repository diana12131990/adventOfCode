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
    mirror_pos = (len(pattern) - 1)//2
    if DetectMirrorline(pattern, mirror_pos):
        Found = True
    else:
        left_pos = mirror_pos - 1
        right_pos = mirror_pos + 1
        while not Found and (left_pos >=0 or right_pos <= (len(pattern) - 2)):
            if left_pos >= 0:
                Found = DetectMirrorline(pattern, left_pos)
                if Found:
                    mirror_pos = left_pos
                    break
                else:
                    left_pos -= 1
                    
            if right_pos <= (len(pattern) - 2):
                Found = DetectMirrorline(pattern, right_pos)
                if Found:
                    mirror_pos = right_pos
                    break
                else:
                    right_pos += 1
    if Found:
        return (mirror_pos + 1)*100
    else:
        # Find mirror pos in colume
        mirror_pos = (len(pattern[0]) - 1)//2
        if DetectMirrorPos(pattern, mirror_pos):
            return mirror_pos+1
        else:
            left_pos = mirror_pos - 1
            right_pos = mirror_pos + 1
            while left_pos >=0 or right_pos <= (len(pattern[0]) - 2):
                if left_pos >= 0:
                    Found = DetectMirrorPos(pattern, left_pos)
                    if Found:
                        mirror_pos = left_pos
                        break
                    else:
                        left_pos -= 1
                        
                if right_pos <= (len(pattern[0]) - 2):
                    Found = DetectMirrorPos(pattern, right_pos)
                    if Found:
                        mirror_pos = right_pos
                        break
                    else:
                        right_pos += 1                
            return mirror_pos+1
    
    
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