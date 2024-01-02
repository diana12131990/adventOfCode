import re

f = open("day_22_input.txt","r")

cube_map = []
cubes = []
c_num = 1

# get original cube map
for line in f:
    line = line.strip()
    start,end = re.split("~",line)
    start = re.split(",",start)
    for i in range(len(start)):
        start[i] = int(start[i])
    end = re.split(",",end)
    for i in range(len(end)):
        end[i] = int(end[i])    
    
    x_length = end[0]-start[0]+1
    y_length = end[1]-start[1]+1
    z_length = end[2]-start[2]+1
    if x_length > 1:
        cubes.append(["x",x_length])
    else:
        if y_length > 1:
            cubes.append(["y",y_length])
        else:
            cubes.append(["z",z_length])  
        
    for x_range in range(x_length):
        x = start[0]+x_range 
        for y_range in range(y_length):
            y = start[1]+y_range 
            for z_range in range(z_length):
                z = start[2]+z_range               
                if len(cube_map) <= z:
                    for i in range(z-len(cube_map)+1):
                        xy_map = []
                        for j in range(10):
                            xy_map.append([0]*10)
                        cube_map.append(xy_map)
                cube_map[z][x][y] = c_num
    c_num += 1    
f.close()

# move cubes
def moveCubes(x,y,z,c_num,cube):
    axis = cube[0]
    length = cube[1]
    if z > 0:
        while z > 0:
            if axis == "z":
                if cube_map[z-1][x][y] == 0:
                    cube_map[z-1][x][y] = c_num
                    cube_map[z+length-1][x][y] = 0
                    z -= 1
                else:
                    break
            else:
                stop = False
                for l_range in range(length):
                    if axis == "x":
                        if cube_map[z-1][x+l_range][y] != 0:
                            stop = True
                            break
                    elif axis == "y":
                        if cube_map[z-1][x][y+l_range] != 0:
                            stop = True
                            break
                if stop:
                    break
                else:
                    for l_range in range(length):
                        if axis == "x":
                            cube_map[z-1][x+l_range][y] = c_num
                            cube_map[z][x+l_range][y] = 0
                        elif axis == "y":
                            cube_map[z-1][x][y+l_range] = c_num
                            cube_map[z][x][y+l_range] = 0                            
                    z -= 1    
    

for z in range(len(cube_map)):
    for x in range(len(cube_map[z])):
        for y in range(len(cube_map[z][x])):
            if cube_map[z][x][y] != 0:
                c_num = cube_map[z][x][y]
                i = c_num - 1
                moveCubes(x, y, z, c_num, cubes[i])

for z in reversed(cube_map):
    all_zero = True
    for x in z:
        for y in x:
            if y > 0:
                all_zero = False
                break
        if not all_zero:
            break
    
    if all_zero:
        cube_map.remove(z)
    else:
        break

# remove each cube and see if it still stand
def GetCubeInfo(i):
    c_num = i+1
    axis = cubes[i][0]
    length = cubes[i][1]
    for z in range(len(cube_map)):
        for x in range(len(cube_map[z])):
            if c_num in cube_map[z][x]:
                for y in range(len(cube_map[z][x])):
                    if c_num == cube_map[z][x][y]:
                        return axis,length,x,y,z

def SafeCheck(check_c_num,remove_c_num):
    h_c_i = check_c_num - 1
    h_axis,h_length,h_x,h_y,h_z = GetCubeInfo(h_c_i)
    if h_axis != "z":
        if h_axis == "x":
            for i_range in range(h_length):
                if cube_map[h_z-1][h_x+i_range][h_y] != 0 and cube_map[h_z-1][h_x+i_range][h_y] != remove_c_num:
                    return True 
        else:
            for i_range in range(h_length):
                if cube_map[h_z-1][h_x][h_y+i_range] != 0 and cube_map[h_z-1][h_x][h_y+i_range] != remove_c_num:
                    return True
    return False

save = 0
for i in range(len(cubes)):
    c_num = i+1
    axis,length,x,y,z = GetCubeInfo(i)
    
    if axis == "z":
        if z+length == len(cube_map):
            save += 1
        else:
            if cube_map[z+length][x][y] == 0:
                save += 1
            else:
                if SafeCheck(cube_map[z+length][x][y], c_num):
                    save += 1
    else:
        if z+1 == len(cube_map):
            save += 1
        else:
            h_cubes = []
            safe = True
            for i_range in range(length):
                if axis == "x":
                    h_c_num = cube_map[z+1][x+i_range][y]
                else:
                    h_c_num = cube_map[z+1][x][y+i_range]
                    
                if h_c_num != 0 and h_c_num not in h_cubes:
                    h_cubes.append(h_c_num)
                    if not SafeCheck(h_c_num, c_num):
                        safe = False
                        break
            if safe:
                save += 1
                        
print(save)