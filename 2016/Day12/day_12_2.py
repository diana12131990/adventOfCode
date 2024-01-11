import re

f = open("day_12_input.txt","r")

password= {
    "c":1
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
        if line[1].isdigit():
            password[line[2]] = int(line[1])
        else:
            password[line[2]] = password[line[1]]
        i += 1
        
    elif action == "inc":
        password[line[1]] += 1
        i += 1
        
    elif action == "dec":
        password[line[1]] -= 1
        i += 1
        
    elif action == "jnz":
        if line[1].isdigit():
            if int(line[1]) != 0:
                i += int(line[2])
            else:
                i += 1
        else:
            if not password.has_key(line[1]):
                password.update({line[1]:0})
            if password[line[1]] != 0:
                i += int(line[2])
            else:
                i += 1
        
print(password["a"])