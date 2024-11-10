import re
from functools import lru_cache

f = open("day_16_input.txt","r")

line = f.readline()
line = line.strip()
dance_move = line.split(",")

program = ''.join(chr(i) for i in range(ord('a'),ord('p')+1))

@lru_cache(maxsize=None)
def dancing(program,s):

    if s[0] == "s":         # spin
        size = int(s[1:]) * -1
        return program[size:] + program[:size]
        
    
    elif s[0] == "x":       # exchange
        positions = s[1:].split("/")
        i = int(positions[0])
        j = int(positions[1])
        lst = list(program)
        lst[i], lst[j] = lst[j], lst[i]
        return ''.join(lst)
        
        
    elif s[0] == "p":       # partner
        characters = s[1:].split("/")
        x = characters[0]
        y = characters[1]
        return program.replace(x,"z").replace(y,x).replace("z",y)
    
    

for i in range(1000000000):
    for step in dance_move:
        program = dancing(program,step)
    
    print(i+1,":",program)