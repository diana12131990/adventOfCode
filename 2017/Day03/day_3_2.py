
input_num = 277678

pos = [[0,0]]
value = [1]
direction = ">"
time = 1

def ChangeDirAndTime():
    global direction
    global time
    
    if direction == ">":
        direction = "^"
    elif direction == "^":
        direction = "<"
        time += 1
    elif direction == "<":
        direction = "v"
    elif direction == "v":
        direction = ">"
        time += 1

while value[-1] < input_num:
    
    for x in range(time):
        l_pos = pos[-1]
        i = l_pos[0]
        j = l_pos[1]
        
        if direction == ">":
            j += 1
        elif direction == "^":
            i -= 1
        elif direction == "<":
            j -= 1
        elif direction == "v":
            i += 1
        
        new_value = 0
        if [i-1,j-1] in pos:
            new_value += value[pos.index([i-1,j-1])]
        if [i-1,j] in pos:
            new_value += value[pos.index([i-1,j])]
        if [i-1,j+1] in pos:
            new_value += value[pos.index([i-1,j+1])]
        if [i,j-1] in pos:
            new_value += value[pos.index([i,j-1])]
        if [i,j+1] in pos:
            new_value += value[pos.index([i,j+1])]
        if [i+1,j-1] in pos:
            new_value += value[pos.index([i+1,j-1])]
        if [i+1,j] in pos:
            new_value += value[pos.index([i+1,j])]
        if [i+1,j+1] in pos:
            new_value += value[pos.index([i+1,j+1])]
        
        pos.append([i,j])
        value.append(new_value)
        
        if value[-1] > input_num:
            break
            
    ChangeDirAndTime()

print(value[-1])