import re

f = open("day_15_input.txt","r")

box_map = []
direction = ""
map_done = False
i = 0
j = 0
for line in f:
    line = line.strip()
    if line == "":
        map_done = True
    else:
        if not map_done:
            newline = ""
            for x in line:
                if x == "#":
                    newline += "##"
                elif x == ".":
                    newline += ".."
                elif x == "@":
                    newline += "@."
                elif x == "O":
                    newline += "[]"
            box_map.append(list(newline))
            if "@" in newline:
                i = len(box_map)-1
                j = newline.index("@")
        else:
            direction += line
f.close()

direction = list(direction)

def DetectHorizon(i,j,y):
    if box_map[i][j+y] != "#":
        box_move = 0
        check_i,check_j = i, j+y
        while box_map[check_i][check_j] == "]" or box_map[check_i][check_j] == "[":
            box_move += 1
            check_j += y
        if box_map[check_i][check_j] != "#":
            if box_move != 0:
                if y < 0:
                    while check_j < j+y:
                        box_map[check_i][check_j] = "["
                        check_j -= y
                        box_map[check_i][check_j] = "]"
                        check_j -= y
                else:
                    while check_j > j+y:
                        box_map[check_i][check_j] = "]"
                        check_j -= y
                        box_map[check_i][check_j] = "["
                        check_j -= y                    
            box_map[i][j+y] = "@"
            box_map[i][j] = "."
            return True
    return False

def DetectVerticle(i,j,x):
    blocked = False
    moving_box_left_pos = []
    moving_box_right_pos = []        
    check_i = i+x
    check_j_list= [j]
    while not blocked:
        moveable = True
        test_j = check_j_list.copy()
        for check_j in test_j:
            if box_map[check_i][check_j] == "[":
                moveable = False
                check_j_list.append(check_j+1)
                moving_box_left_pos.append((check_i,check_j))
                moving_box_right_pos.append((check_i,check_j+1))
            elif box_map[check_i][check_j] == "]":
                moveable = False
                check_j_list.append(check_j-1)
                check_j_list = sorted(check_j_list)
                moving_box_left_pos.append((check_i,check_j-1))
                moving_box_right_pos.append((check_i,check_j))
            elif box_map[check_i][check_j] == "#":
                blocked = True
                break
            elif box_map[check_i][check_j] == ".":
                check_j_list.remove(check_j)
        
        if moveable:
            break
        else:
            check_i += x
        
        
    if not blocked:
        if len(moving_box_left_pos) != 0:
            for (l_i,l_j) in moving_box_left_pos:
                box_map[l_i+x][l_j] = "["
                if (l_i-x,l_j) not in moving_box_left_pos and (l_i-x,l_j) not in moving_box_right_pos:
                    box_map[l_i][l_j] = "."
            for (r_i,r_j) in moving_box_right_pos:
                box_map[r_i+x][r_j] = "]"
                if (r_i-x,r_j) not in moving_box_left_pos and (r_i-x,r_j) not in moving_box_right_pos:
                    box_map[r_i][r_j] = "."                
        box_map[i+x][j] = "@"
        box_map[i][j] = "."
        return True
    return False

step = 0
for d in direction:
    if d == "<" and DetectHorizon(i,j,-1):
        j -= 1
    elif d == "^" and DetectVerticle(i,j,-1):
        i -= 1
    elif d == ">" and DetectHorizon(i,j,1):
        j += 1
    elif d == "v" and DetectVerticle(i,j,1):
        i += 1
    
result = 0
for x in range(len(box_map)):
    line = box_map[x]
    if "[" in line:
        indices = [y for y, char in enumerate(line) if char == "["]
        for y in indices:
            result += 100*x+y
print(result)