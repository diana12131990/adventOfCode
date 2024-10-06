import re

f = open("day_12_input.txt","r")

program = []
for line in f:
    line = line.strip()
    _,connection = re.split(" <-> ",line)
    connection = re.findall("\d+",connection)
    connection = [int(x) for x in connection]
    program.append(connection)

connect_group = [0]
i = 0
while i < len(connect_group):
    connect_i = connect_group[i]
    new_connect = program[connect_i]
    for n in new_connect:
        if n not in connect_group:
            connect_group.append(n)
    i += 1
    
print(len(connect_group))