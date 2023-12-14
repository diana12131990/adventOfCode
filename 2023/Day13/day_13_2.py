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

def GetReflectionSum(pattern,old_pos):
    Found = False
    # Find mirror pos in row
    mirror_pos = 0
    while not Found and mirror_pos <= (len(pattern) - 2):       
        Found = DetectMirrorline(pattern, mirror_pos)
        if Found:
            if old_pos == [mirror_pos,"row"]:
                Found = False
                mirror_pos += 1
            else:
                return [mirror_pos,"row"]
        else:
            mirror_pos += 1
                    
    # Find mirror pos in column
    mirror_pos = 0
    while not Found and mirror_pos <= (len(pattern[0]) - 2):
        Found = DetectMirrorPos(pattern, mirror_pos)
        if Found:
            if old_pos == [mirror_pos,"column"]:
                Found = False
                mirror_pos += 1
            else:                        
                return [mirror_pos,"column"]
        else:
            mirror_pos += 1                
        
    return [-1,"None"]
    
    
pattern = []
old_pos = [-1,"None"]
reflection_sum = 0

for line in f:
    line = line.strip()
    
    if line == "":
        old_pos = GetReflectionSum(pattern,old_pos)
        
        Found = False
        for i in range(len(pattern)):
            if Found:
                break
            for j in range(len(pattern[0])):
                fixed_pattern = pattern[:]
                string_list = list(pattern[i])
                if pattern[i][j] == ".":
                    string_list[j] = "#"
                else:
                    string_list[j] = "."
                fixed_pattern[i]= "".join(string_list)
                
                new_pos = GetReflectionSum(fixed_pattern, old_pos)
                if new_pos != [-1,"None"]:
                    Found = True
                    if new_pos[1] == "row":
                        reflection_sum+= (new_pos[0]+1)*100
                    else:
                        reflection_sum+= (new_pos[0]+1)
                    break
                
        pattern = []
        old_pos = [-1,"None"]
    else:
        pattern.append(line)

old_pos = GetReflectionSum(pattern,old_pos)   
Found = False
for i in range(len(pattern)):
    if Found:
        break
    for j in range(len(pattern[0])):
        fixed_pattern = pattern[:]
        string_list = list(pattern[i])
        if pattern[i][j] == ".":
            string_list[j] = "#"
        else:
            string_list[j] = "."
        fixed_pattern[i]= "".join(string_list)
        new_pos = GetReflectionSum(fixed_pattern, old_pos)
        if new_pos != [-1,"None"]:
            Found = True
            if new_pos[1] == "row":
                reflection_sum+= (new_pos[0]+1)*100
            else:
                reflection_sum+= (new_pos[0]+1)
            break
        
print(reflection_sum)
f.close()