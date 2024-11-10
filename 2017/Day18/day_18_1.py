import re

f = open("day_18_input.txt","r")

sounds= {}
instructions = []
for line in f:
    line = line.strip()
    line = line.split()
    instructions.append(line)
f.close()

i = 0
played = 0
while i < len(instructions):
    line = instructions[i]
    action = line[0]
    if action == "snd":             # Play sound
        played = sounds[line[1]]
        i += 1
        
    elif action == "set":           # Set X with Y
        if line[2].isdigit() or line[2][0] == "-":
            sounds.update({line[1]:int(line[2])})
        else:
            sounds.update({line[1]:sounds[line[2]]})
        i += 1
            
    elif action == "add":           # Add Y to X's value
        if line[1] not in sounds:
            sounds.update({line[1]:0})
            
        if line[2].isdigit() or line[2][0] == "-":
            sounds[line[1]] += int(line[2])
        else:
            sounds[line[1]] += sounds[line[2]]
        i += 1
    
    elif action == "mul":           # Multiply Y to X's Value
        if line[1] not in sounds:
            sounds.update({line[1]:0})
        elif sounds[line[1]] != 0:
            if line[2].isdigit() or line[2][0] == "-":
                sounds[line[1]] *= int(line[2])
            else:
                sounds[line[1]] *= sounds[line[2]]
        i += 1
        
    elif action == "mod":           # Remain after X's Value divided by Y
        if line[1] not in sounds:
            sounds.update({line[1]:0})
        elif sounds[line[1]] != 0:
            if line[2].isdigit() or line[2][0] == "-":
                sounds[line[1]] %= int(line[2])
            else:
                sounds[line[1]] %= sounds[line[2]]
        i += 1  
    
    elif action == "rcv":           # Recover X's value to previous played, and finish
        if line[1] in sounds:
            if sounds[line[1]] != 0:
                sounds.update({line[1]:played})
                print(sounds[line[1]])
                break
        i += 1     
    
    elif action == "jgz":           # Jump instruction
        if line[1] in sounds:
            if sounds[line[1]] > 0:
                i += int(line[2])
            else:
                i += 1
        else:
            i += 1