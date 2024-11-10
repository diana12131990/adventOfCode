import re

f = open("day_16_input.txt","r")

line = f.readline()
line = line.strip()
dance_move = line.split(",")
f.close()

program = ''.join(chr(i) for i in range(ord('a'),ord('p')+1))

for s in dance_move:
    if s[0] == "s":         # spin
        size = int(s[1:]) * -1
        program = program[size:] + program[:size]
    
    elif s[0] == "x":       # exchange
        positions = s[1:].split("/")
        i = int(positions[0])
        j = int(positions[1])
        
        lst = list(program)
        lst[i], lst[j] = lst[j], lst[i]
        program = ''.join(lst)
        
    elif s[0] == "p":       # partner
        characters = s[1:].split("/")
        x = characters[0]
        y = characters[1]
        program = program.replace(x,"z").replace(y,x).replace("z",y)

print(program)