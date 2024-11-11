import re

f = open("day_18_input.txt","r")

instructions = []
for line in f:
    line = line.strip()
    line = line.split()
    instructions.append(line)
f.close()

program_0 = {
    "p":0
}
program_send_0 = []
i = 0
p0_running = True

program_1= {
    "p":1
}
program_send_1 = []
j = 0
p1_running = True
p1_send_amount = []


def running_instruction(program, program_id, index):
    line = instructions[index]
    action = line[0]
    if action == "snd":                                         # Save value to queue for sending to other
        if line[1].isdigit() or line[1][0] == "-":
            value = int(line[1])
        else:
            value = program[line[1]]
            
        if program_id == 0:
            program_send_0.append(value)
        else:
            program_send_1.append(value)
            p1_send_amount.append(value)
        return (program,index+1,True) 
        
    elif action == "set":                                       # Set X with Y
        if line[2].isdigit() or line[2][0] == "-":
            program.update({line[1]:int(line[2])})
        else:
            program.update({line[1]:program[line[2]]})
        return (program,index+1,True) 
            
    elif action == "add":                                       # Add Y to X's value
        if line[1] not in program:
            program.update({line[1]:0})
            
        if line[2].isdigit() or line[2][0] == "-":
            program[line[1]] += int(line[2])
        else:
            if line[2] not in program:
                program.update({line[2]:0})
            else:
                program[line[1]] += program[line[2]]
        return (program,index+1,True) 
    
    elif action == "mul":                                       # Multiply Y to X's Value
        if line[1] not in program:
            program.update({line[1]:0})
        elif program[line[1]] != 0:
            if line[2].isdigit() or line[2][0] == "-":
                program[line[1]] *= int(line[2])
            else:
                if line[2] not in program:
                    program.update({line[2]:0})                
                program[line[1]] *= program[line[2]]
        return (program,index+1,True) 
        
    elif action == "mod":                                       # Remain after X's Value divided by Y
        if line[1] not in program:
            program.update({line[1]:0})
        elif program[line[1]] != 0:
            if line[2].isdigit() or line[2][0] == "-":
                program[line[1]] %= int(line[2])
            else:
                if line[2] not in program:
                    program.update({line[2]:0})
                else:
                    program[line[1]] %= program[line[2]]
        return (program,index+1,True)
    
    elif action == "rcv":                                       # receive value from other's queue and set to X
        if line[1] not in program:
            program.update({line[1]:0})
            
        if program_id == 0:
            if program_send_1 != []:
                program.update({line[1]:program_send_1[0]})
                program_send_1.pop(0)
                return (program,index+1,True)
            else:
                return (program,index,False)
        else:
            if program_send_0 != []:
                program.update({line[1]:program_send_0[0]})
                program_send_0.pop(0)
                return (program,index+1,True)
            else:
                return (program,index,False)
    
    elif action == "jgz":                                       # Jump instruction
        if line[1] in program:
            if program[line[1]] > 0:
                if line[2].isdigit() or line[2][0] == "-":
                    return (program,index+int(line[2]),True)
                else:
                    return (program,index+program[line[2]],True)
            else:
                return (program,index+1,True)
        else:
            return (program,index+1,True) 
        

while p0_running or p1_running:
    if i < len(instructions):
        (program_0,i,p0_running) = running_instruction(program_0,0,i)
        print("0",program_0,len(program_send_0),i)
    else:
        p0_running = False
        
    if j < len(instructions):
        (program_1,j,p1_running) = running_instruction(program_1,1,j)
        print("1",program_1,len(program_send_1),j)
    else:
        p1_running = False
        
print(len(p1_send_amount))