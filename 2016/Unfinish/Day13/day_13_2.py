favorite_num = 1364
pos = []

def CountOneInBinary(x,y):
    value = bin(x*x + 3*x + 2*x*y + y + y*y + favorite_num)
    one_amount = value.count("1")
    if one_amount%2 == 0:
        return True
    else:
        return False   

def AddRow(r_target):
    for y in range(len(building_map),r_target+1):
        building_map.append([])
        for x in range(len(building_map[0])):
            if CountOneInBinary(x,y):
                building_map[y].append(".")
            else:
                building_map[y].append("#")            

def AddColumn(c_target):
    original_len = len(building_map[0])
    for y in range(len(building_map)):
        for x in range(original_len,c_target+1):
            if CountOneInBinary(x,y):
                building_map[y].append(".")
            else:
                building_map[y].append("#")            

def FindSteps(i,j,d,s):
    
    if [i,j] not in pos:
        pos.append([i,j])
        
    if s < 50:
        s += 1
        if j >= len(building_map[0])-1:
            AddColumn(j)
        if i >= len(building_map)-1:
            AddRow(i)
        
        if d == ">":
            if building_map[i][j+1] == ".":
                building_map[i][j+1] = "O"
                FindSteps(i,j+1,">",s)
                building_map[i][j+1] = "."
                
            if building_map[i+1][j] == ".":
                building_map[i+1][j] = "O"
                FindSteps(i+1,j,"v",s)
                building_map[i+1][j] = "."
                
            if building_map[i-1][j] == ".":
                building_map[i-1][j] = "O"
                FindSteps(i-1,j,"^",s)
                building_map[i-1][j] = "."
                
        if d == "v":
            if building_map[i][j+1] == ".":
                building_map[i][j+1] = "O"
                FindSteps(i,j+1,">",s)
                building_map[i][j+1] = "."
                
            if building_map[i+1][j] == ".":
                building_map[i+1][j] = "O"
                FindSteps(i+1,j,"v",s)
                building_map[i+1][j] = "."
                
            if building_map[i][j-1] == ".":
                building_map[i][j-1] = "O"
                FindSteps(i,j-1,"<",s)
                building_map[i][j-1] = "."
                
        if d == "<":
            if building_map[i+1][j] == ".":
                building_map[i+1][j] = "O"
                FindSteps(i+1,j,"v",s)
                building_map[i+1][j] = "."
                
            if building_map[i][j-1] == ".":
                building_map[i][j-1] = "O"
                FindSteps(i,j-1,"<",s)
                building_map[i][j-1] = "."
                
            if building_map[i-1][j] == ".":
                building_map[i-1][j] = "O"
                FindSteps(i-1,j,"^",s)
                building_map[i-1][j] = "."  
                
        if d == "^":
            if building_map[i][j+1] == ".":
                building_map[i][j+1] = "O"
                FindSteps(i,j+1,">",s)
                building_map[i][j+1] = "."
                
            if building_map[i][j-1] == ".":
                building_map[i][j-1] = "O"
                FindSteps(i,j-1,"<",s)
                building_map[i][j-1] = "."
                
            if building_map[i-1][j] == ".":
                building_map[i-1][j] = "O"
                FindSteps(i-1,j,"^",s)
                building_map[i-1][j] = "."         

i = 1
j = 1
building_map = []

for y in range(70):
    building_map.append([])
    for x in range(70):
        if CountOneInBinary(x,y):
            building_map[y].append(".")
        else:
            building_map[y].append("#")


building_map[i][j] = "O"
pos.append([i,j])
if building_map[i][j+1] == ".":
    building_map[i][j+1] = "O"
    FindSteps(i,j+1,">",1)
    building_map[i][j+1] = "."
    
if building_map[i+1][j] == ".":
    building_map[i+1][j] = "O"
    FindSteps(i+1,j,"v",1)
    building_map[i+1][j] = "."
    
if building_map[i][j-1] == ".":
    building_map[i][j-1] = "O"
    FindSteps(i,j-1,"<",1)
    building_map[i][j-1] = "."
    
if building_map[i+1][j] == ".":
    building_map[i+1][j] = "O"
    FindSteps(i+1,j,"^",1)
    building_map[i+1][j] = "."
    
print(len(pos))