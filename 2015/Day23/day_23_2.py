import re

a = 1
b = 0
f = open("day_23_input.txt","r")
instruction = []

for line in f:
    line = line.strip()
    action = line[:3]
    line = line[4:]
    if action != "jmp":
        r = line[0]
        if "," in line:
            num = re.findall("-?\d+",line)
            num = int(num[0])
            instruction.append([action,r,num])
        else:
            instruction.append([action,r])
    else:
        num = re.findall("-?\d+",line)
        num = int(num[0])
        instruction.append([action,num])        
f.close()

i = 0
while i != len(instruction):
    line = instruction[i]
    print(line)
    action = line[0]
    
    if action == "hlf":
        if line[1] == "a":
            a /= 2
        else:
            b /= 2
        i += 1
            
    elif action == "tpl":
        if line[1] == "a":
            a *= 3
        else:
            b *= 3
        i += 1
        
    elif action == "inc":
        if line[1] == "a":
            a += 1
        else:
            b += 1
        i += 1
        
    elif action == "jmp":
        i += line[1]
    
    elif action == "jie":
        if (line[1] == "a" and a%2 == 0) or (line[1] == "b" and b%2 == 0):
            i += line[2]
        else:
            i += 1
    
    elif action == "jio":
        if (line[1] == "a" and a == 1) or (line[1] == "b" and b == 1):
            i += line[2]
        else:
            i += 1
    else:
        print("ERROR")
        break
    
    print(a,b)