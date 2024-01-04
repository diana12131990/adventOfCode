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

    if c_dir == "Down":
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
        
def CountLand(line,left,right):
    if left+1 == right:
        return 0
    else:
        l_count = 0
        for x in range(right-left-1):
            index = x + left +1
            if line[index] == ".":
                l_count += 1
        return l_count

f = open("day_10_input.txt","r")
p_map = []
l_map = []
l_pos = []
i = -1
j = -1
p_dir = "Unknown"

row = 0
for line in f:
    line = line.strip()
    p_map.append(list(line))
    if "S" in line:
        i = row
        j = p_map[i].index("S")
        l_pos.append([i,j])
    row += 1
f.close()

p_dir = FindStartDirection(p_map,i,j)
for x in range(row):
    loop_list = [0] * len(p_map[0])
    if x == i:
        loop_list[j] = 1
    l_map.append(loop_list)

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
    l_pos.append([i,j])
    p_dir = FindDirection(p_dir,p_map[i][j])   
    l_map[i][j] = 1
    if p_dir == "Back":
        isBack = True
        
# Question 2
inside_pos = []
def AddInsideTile(i,j):
    if 0 <= i < len(l_map) and 0 <= j < len(l_map[0]):
        if l_map[i][j] == 0 and [i,j] not in inside_pos:
            if i == 0 or i == len(l_map)-1 or j == 0 or j == len(l_map[0])-1:
                return False
            inside_pos.append([i,j])
    return True

def FloodFill():
    index = 0
    while True:
        if index >= len(inside_pos):
            break
        pos = inside_pos[index]
        i = pos[0]
        j = pos[1]
        if p_map[i][j] == 0:
            if i > 0:
                inside_pos.append([i-1,j])
            if i < len(p_map) - 1:
                inside_pos.append([i+1,j])
            if j > 0:
                inside_pos.append([i,j-1])
            if j < len(p_map[0]) - 1:
                inside_pos.append([i,j+1])
        index += 1

pre_pos = l_pos[0]
at_inside = True
for index in range(len(l_pos)-1):
    pos = l_pos[index+1]
    i = pos[0]
    j = pos[1]
    pre_i = pre_pos[0]
    pre_j = pre_pos[1]
    n_pipe = p_map[i][j]
    
    if n_pipe == '|':
        if pre_i > i:
            at_inside = AddInsideTile(i,j+1)
            if not at_inside:
                break
        else:
            at_inside = AddInsideTile(i,j-1)
            if not at_inside:
                break
    elif n_pipe == '-':
        if pre_j < j:
            at_inside = AddInsideTile(i+1,j)
            if not at_inside:
                break
        else:
            at_inside = AddInsideTile(i-1,j)
            if not at_inside:
                break
    elif n_pipe == 'F':
        if pre_j > j:
            at_inside = AddInsideTile(i-1,j) 
            if not at_inside:
                break
            at_inside = AddInsideTile(i,j-1) 
            if not at_inside:
                break
    elif n_pipe == 'L':
        if pre_i < i:
            at_inside = AddInsideTile(i+1,j)
            if not at_inside:
                break
            at_inside = AddInsideTile(i,j-1)
            if not at_inside:
                break
    elif n_pipe == 'J':
        if pre_j < j:
            at_inside = AddInsideTile(i+1,j)
            if not at_inside:
                break
            at_inside = AddInsideTile(i,j+1)
            if not at_inside:
                break
    elif n_pipe == '7':
        if pre_i > i:
            at_inside = AddInsideTile(i-1,j)
            if not at_inside:
                break
            at_inside = AddInsideTile(i,j+1)
            if not at_inside:
                break
    pre_pos = pos
if at_inside:
    FloodFill()
else:
    # Reverse
    inside_pos = []
    pre_pos = l_pos[0]
    for index in range(len(l_pos)-1):
        pos = l_pos[index+1]
        i = pos[0]
        j = pos[1]
        pre_i = pre_pos[0]
        pre_j = pre_pos[1]
        n_pipe = p_map[i][j]
        
        if n_pipe == '|':
            if pre_i > i:
                at_inside = AddInsideTile(i,j-1)
            else:
                at_inside = AddInsideTile(i,j+1)
        elif n_pipe == '-':
            if pre_j < j:
                at_inside = AddInsideTile(i-1,j)
            else:
                at_inside = AddInsideTile(i+1,j)  
        elif n_pipe == 'F':
            if pre_i > i:
                at_inside = AddInsideTile(i-1,j) 
                at_inside = AddInsideTile(i,j-1)    
        elif n_pipe == 'L':
            if pre_j > j:
                at_inside = AddInsideTile(i+1,j)
                at_inside = AddInsideTile(i,j-1)
        elif n_pipe == 'J':
            if pre_i < i:
                at_inside = AddInsideTile(i+1,j)
                at_inside = AddInsideTile(i,j+1)
        elif n_pipe == '7':
            if pre_j < j:
                at_inside = AddInsideTile(i-1,j)
                at_inside = AddInsideTile(i,j+1)
        pre_pos = pos
    FloodFill()

print(len(inside_pos))