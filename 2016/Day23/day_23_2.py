import re

f = open("day_23_input.txt","r")

password= {
    "a":12
}
instructions = []
for line in f:
    line = line.strip()
    line = line.split()
    instructions.append(line)
    
f.close()

i = 0
while i < len(instructions):
    line = instructions[i]
    action = line[0]
    if action == "cpy":
        if not password.has_key(line[2]):
            password.update({line[2]:0})
        if line[1].isdigit() or "-" in line[1]:
            password[line[2]] = int(line[1])
        else:
            if not password.has_key(line[1]):
                password.update({line[1]:0})
            password[line[2]] = password[line[1]]
        i += 1
        
    elif action == "inc":
        if not password.has_key(line[1]):
            password.update({line[1]:0})
        password[line[1]] += 1
        i += 1
        
    elif action == "dec":
        if not password.has_key(line[1]):
            password.update({line[1]:0})        
        password[line[1]] -= 1
        i += 1
        
    elif action == "jnz":
        check_num = 0
        if line[1].isdigit() or "-" in line[1]:
            check_num = int(line[1])
        else:
            if not password.has_key(line[1]):
                password.update({line[1]:0}) 
            check_num = password[line[1]]
            
        step = 0
        if line[2].isdigit() or "-" in line[2]:
            step = int(line[2])
        else:
            if not password.has_key(line[2]):
                password.update({line[2]:0}) 
            step = password[line[2]]  
                    
        if  check_num != 0 and step != 0:
            i += step
        else:
            i += 1
                
    elif action == "tgl":
        step = 0
        if line[1].isdigit() or "-" in line[1]:
            if int(line[1]) != 0:
                step = int(line[1])
        else:
            if not password.has_key(line[1]):
                password.update({line[1]:0})
            step = password[line[1]]
        
        if step != 0:
            j = i+step
            if j < len(instructions):
                if len(instructions[j]) == 2:
                    if not instructions[j][1].isdigit() or "-" not in instructions[j][1]:
                        if instructions[j][0] == "inc":
                            instructions[j][0] = "dec"
                        else:
                            instructions[j][0] = "inc"
                elif len(instructions[j]) == 3:
                    if instructions[j][0] == "jnz":
                        if not instructions[j][2].isdigit() or "-" not in instructions[j][2]:
                            instructions[j][0] = "cpy"
                    else:
                        instructions[j][0] = "jnz"
        i += 1
    print(password)
print(password["a"])