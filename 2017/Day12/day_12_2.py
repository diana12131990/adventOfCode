import re

f = open("day_12_input.txt","r")

program = []
for line in f:
    line = line.strip()
    _,connection = re.split(" <-> ",line)
    connection = re.findall("\d+",connection)
    connection = [int(x) for x in connection]
    program.append(connection)


total_group = []
remain_line = [x for x in range(len(program))]
while len(remain_line) > 0:
    
    i = 0
    connect_group = [remain_line[0]]
    remain_line.pop(0)
    
    while i < len(connect_group):
        connect_i = connect_group[i]
        new_connect = program[connect_i]
        for n in new_connect:
            if n not in connect_group:
                connect_group.append(n)
                remain_line.remove(n)
        i += 1
    total_group.append(connect_group)
     
print(len(total_group))