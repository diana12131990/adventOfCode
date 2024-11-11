import re

f = open("day_2_input.txt","r")

count_2 = 0
count_3 = 0


for line in f:
    line = line.strip()
    character_list = {}

    count_2_found = False
    count_3_found = False

    for c in line:
        if c in character_list:
            character_list[c] += 1
        else:
            character_list[c] = 1

    for i in character_list.values():
        if i == 2 and not count_2_found:
            count_2 += 1
            count_2_found = True
        elif i == 3 and not count_3_found:
            count_3 += 1
            count_3_found = True

        if count_2_found and count_3_found:
            break

print(count_2*count_3)