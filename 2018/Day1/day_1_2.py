import re
f = open("day_1_input.txt","r")

current_f = []
for line in f:
    current_f.append(int(line))
f.close()

i = 0
total = 0
frequency_list = []

while(True):
    total += current_f[i]
    i += 1
    if i == len(current_f):
        i = 0
        
    if total not in frequency_list:
        frequency_list.append(total)
    else:
        print(total)
        break