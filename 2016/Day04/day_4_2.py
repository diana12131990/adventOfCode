import re

f = open("day_4_input.txt","r")

real_room = []
for line in f:
    line = line.strip()
    line,checksum = re.split("\[",line)
    checksum = checksum.replace("]","")
    section_id = re.findall("\d+",line)
    section_id = int(section_id[0])
    name = line.replace(str(section_id),"")
    name = name.replace("-"," ")
    
    count_list = {}
    for x in name:
        if x != " ":
            if not count_list.has_key(x):
                count_list.update({x:0})
            count_list[x] += 1
    key_list = list(count_list.keys())
    key_list.sort()
    max_number = max(count_list.values())
    
    number_list = {}
    for x in key_list:
        num = count_list[x]
        if not number_list.has_key(num):
            number_list.update({num:""})
        number_list[num] += x
    
    check_string = ""
    while len(check_string) < 5:
        if number_list.has_key(max_number):
            check_string += number_list[max_number]
        max_number -= 1
    if check_string[:5] == checksum:
        real_room.append([name,section_id])
f.close()

for i in range(len(real_room)):
    name = real_room[i][0]
    section_id = real_room[i][1]%26
    
    new_str = ""
    for c in name:
        if c == " ":
            new_str += " "
        else:
            new_c = chr((ord(c) - 97 + section_id) % 26 + 97)
            new_str += new_c
    
    if "north" in new_str:
        print(new_str)
        print(real_room[i][1])
        break