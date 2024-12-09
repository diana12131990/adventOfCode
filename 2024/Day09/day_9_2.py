import re

f = open("day_9_input.txt","r")
line = f.readline()
f.close()

current_id = 0
disk_map = []
file_list = []
free_list = []
for i,x in enumerate(line):
    n = int(x)
    first_index = len(disk_map)
    if i%2 == 0:
        for m in range(n):
            disk_map.append(str(current_id))
        current_id += 1
        file_list.append((first_index,n))
    else:
        disk_map.extend("."*n)
        free_list.append((first_index,n))

for reverse_i,file_data in enumerate(reversed(file_list), start = 1):
    current_id = len(file_list)-reverse_i
    id_index = file_data[0]
    id_amount = file_data[1]
    if current_id != 0 and free_list:
        if id_amount != 0:
            for free_index,free_data in enumerate(free_list):
                if id_amount <= free_data[1]:
                    for i in range(free_data[0],free_data[0] + id_amount):
                        disk_map[i] = str(current_id)
                    for i in range(id_index,id_index + id_amount):
                        disk_map[i] = "."
                        
                    remain = free_data[1] - id_amount
                    new_start = free_data[0] + id_amount
                    free_list[free_index]= (new_start,remain)
                    break
        free_list.pop(-1)


checksum = 0
for i,n in enumerate(disk_map):
    if n != ".":
        checksum += i*int(n)
print(checksum)