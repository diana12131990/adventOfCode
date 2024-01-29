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

def DoCopy(source, target):
    if not password.has_key(target):
        password.update({target:0})
    if source.isdigit() or "-" in source:
        password[target] = int(source)
    else:
        if not password.has_key(source):
            password.update({source:0})
        password[target] = password[source]
        
def DoIncrease(target,step):
    if not password.has_key(target):
        password.update({target:0})
    password[target] += step
    
def DoDecrease(target,step):
    if not password.has_key(target):
        password.update({target:0})
    password[target] -= step
    
def DoJump(condition,step,original):
    check_num = 0
    if condition.isdigit() or "-" in condition:
        check_num = int(condition)
    else:
        if not password.has_key(condition):
            password.update({condition:0}) 
        check_num = password[condition]
        
    if step.isdigit() or "-" in step:
        step = int(step)
    else:
        if not password.has_key(step):
            password.update({step:0}) 
        step = password[step]  
                
    if  check_num != 0:
        if step > 0:
            return original + step
        elif step < 0:
            new_i = original + step
            instruct_for_jump = []
            conditions = [condition]
            loop_amount = 1
            for x in range(new_i,original):
                if instructions[x][0] == "cpy":
                    conditions.append(instructions[x][2])
                    DoCopy(instructions[x][1],instructions[x][2])
                elif instructions[x][0] == "inc" or instructions[x][0] == "dec":
                    if instructions[x][1] not in conditions:
                        instruct_for_jump.append(instructions[x])
                    else:
                        loop_amount *= abs(password[instructions[x][1]])
                else:
                    print("skip" + str(instructions[x]))
                    
            for l in instruct_for_jump:
                if l[0] == "inc":
                    DoIncrease(l[1],loop_amount)
                elif l[0] == "dec":
                    DoDecrease(l[1],loop_amount)
                else:
                    print("error")
            for x in conditions:
                password[x] = 0
            return original + 1                
    else:
        return original + 1

def DoToggle(step,original):
    if step.isdigit() or "-" in step:
        if int(step) != 0:
            step = int(step)
    else:
        if not password.has_key(step):
            password.update({step:0})
        step = password[step]
    
    if step != 0:
        j = original+step
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

i = 0
while i < len(instructions):
    line = instructions[i]
    action = line[0]
    if action == "cpy":
        DoCopy(line[1],line[2])
        i += 1
        
    elif action == "inc":
        DoIncrease(line[1],1)
        i += 1
        
    elif action == "dec":
        DoDecrease(line[1],1)
        i += 1
        
    elif action == "jnz":
        i = DoJump(line[1],line[2],i)
                
    elif action == "tgl":
        DoToggle(line[1],i)
        i += 1
    print(password)
print(password["a"])