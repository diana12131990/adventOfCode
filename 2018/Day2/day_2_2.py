import re

f = open("day_2_input.txt","r")

id_list = []
for line in f:
    line = line.strip()
    id_list.append(line)

common_letters = ""
for x in range(len(id_list)-1):
    s1 = id_list[x]
    for y in range(x+1,len(id_list)):
        s2 = id_list[y]

        same_characters = ""
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                same_characters += s1[i]

        if len(same_characters) > len(common_letters):
            common_letters = same_characters

print(common_letters)