import re

def FindStartDirection(p_map,i,j):
    if i != 0:
        n_pipe = p_map[i-1][j]
        if n_pipe == "|" or n_pipe == "F" or n_pipe == "7":
            return "Up"
        
    if i != len(p_map)-1:
        n_pipe = p_map[i+1][j]
        if n_pipe == "|" or n_pipe == "L" or n_pipe == "J":
            return "Down"
        
    if j != 0:
        n_pipe = p_map[i][j-1]
        if n_pipe == "-" or n_pipe == "L" or n_pipe == "F":
            return "Left"
        
    if j != len(p_map[0])-1:
        n_pipe = p_map[i][j+1]
        if n_pipe == "-" or n_pipe == "7" or n_pipe == "J":
            return "Right"

def FindDirection(c_dir,n_pipe):
    if n_pipe == "S":
        return "Back"
    
    if c_dir == "Up":
        if n_pipe == "|":
            return "Up"
        elif n_pipe == "F":
            return "Right"
        elif n_pipe == "7":
            return "Left"
        
    elif c_dir == "Down":
        if n_pipe == "|":
            return "Down"
        elif n_pipe == "L":
            return "Right"
        elif n_pipe == "J":
            return "Left"
        
    if c_dir == "Left":
        if n_pipe == "-":
            return "Left"
        elif n_pipe == "L":
            return "Up"
        elif n_pipe == "F":
            return "Down"
        
    if c_dir == "Right":
        if n_pipe == "-":
            return "Right"
        elif n_pipe == "J":
            return "Up"
        elif n_pipe == "7":
            return "Down"

f = open("day_10_input.txt","r")
p_map = {}
i = -1
j = -1
p_dir = "Unknown"

row = 0
for line in f:
    line = line.strip()
    p_map.update({row:[x for x in line]})
    if "S" in line:
        i = row
        j = p_map[i].index("S")
    row += 1
f.close()

p_dir = FindStartDirection(p_map,i,j)

step = 0
isBack = False
while not isBack:
    if p_dir == "Up":
        i -= 1
    elif p_dir == "Down":
        i += 1
    elif p_dir == "Left":
        j -= 1
    elif p_dir == "Right":
        j += 1
    p_dir = FindDirection(p_dir,p_map[i][j])   
    
    step += 1
    print(i,j,p_dir)
    
    if p_dir == "Back":
        isBack = True
        
print(step/2)