import re

f = open("day_9_input.txt","r")
line = f.readline()
f.close()

current_id = 0
disk_map = []
free_space = 0
for i,x in enumerate(line):
    n = int(x)
    if i%2 == 0:
        for m in range(n):
            disk_map.append(str(current_id))
        current_id += 1
    else:
        disk_map.extend("."*n)
        free_space += n
        
shift_map = disk_map[:-1*(free_space+1):-1]
shift_map = [file for file in shift_map if file != "."]
disk_map = disk_map[:-1*free_space]

free_indices = [i for i, x in enumerate(disk_map) if x == '.']
for i in free_indices:
    disk_map[i] = shift_map[0]
    shift_map = shift_map[1:]

checksum = 0
for i,n in enumerate(disk_map):
    checksum += i*int(n)
print(checksum)