import re

f = open("day_1_input.txt","r")

line = f.readline()
line = line.strip()
positions = re.split(", ",line)
f.close()

direction = "N"
i = 0
j = 0
trace = []
Found = False
for pos in positions:
    turn_dir = pos[0]
    step = int(pos[1:])
    if turn_dir == "R":
        if direction == "N":
            direction = "E"
        elif direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        else:
            direction = "N"
    else:
        if direction == "N":
            direction = "W"
        elif direction == "W":
            direction = "S"
        elif direction == "S":
            direction = "E"
        else:
            direction = "N"
    
    for x in range(step):
        if direction == "N":
            i -= 1
        elif direction == "E":
            j += 1
        elif direction == "S":
            i += 1
        else:
            j -= 1
    
        if [i,j] not in trace:
            trace.append([i,j])
        else:
            print(abs(i)+abs(j))
            Found = True
            break
    if Found:
        break