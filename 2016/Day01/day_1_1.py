import re

f = open("day_1_input.txt","r")

line = f.readline()
line = line.strip()
positions = re.split(", ",line)
f.close()

direction = "N"
i = 0
j = 0

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
    
    if direction == "N":
        i -= step
    elif direction == "E":
        j += step
    elif direction == "S":
        i += step
    else:
        j -= step
print(abs(i)+abs(j))