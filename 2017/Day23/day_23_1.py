import re

f = open("day_23_input.txt","r")

coprocessor= {chr(i): 0 for i in range(ord('a'), ord('h')+1)}
instructions = []
for line in f:
    line = line.strip()
    line = line.split()
    instructions.append(line)
f.close()

i = 0
mul_time = 0
while i < len(instructions):
    line = instructions[i]
    action = line[0]
    if action == "set":           # Set X with Y
        if line[2].isdigit() or line[2][0] == "-":
            coprocessor.update({line[1]:int(line[2])})
        else:
            coprocessor.update({line[1]:coprocessor[line[2]]})
        i += 1
    
    elif action == "sub":           # Substract X and Y value
        if line[2].isdigit() or line[2][0] == "-":
            coprocessor[line[1]] -= int(line[2])
        else:
            coprocessor[line[1]] -= coprocessor[line[2]]
        i += 1    
    
    elif action == "mul":           # Multiply Y to X's Value
        if coprocessor[line[1]] != 0:
            if line[2].isdigit() or line[2][0] == "-":
                coprocessor[line[1]] *= int(line[2])
            else:
                coprocessor[line[1]] *= coprocessor[line[2]]
        i += 1
        mul_time += 1
        
    elif action == "jnz":           # Jump instruction
        if line[1].isdigit() or line[1][0] == "-":
            if int(line[1]) != 0:
                i += int(line[2])
        elif coprocessor[line[1]] != 0:
            i += int(line[2])
        else:
            i += 1
                
    # print(coprocessor)
            
print(mul_time)