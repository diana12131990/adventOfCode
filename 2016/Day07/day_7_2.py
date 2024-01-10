import re

def CheckABA(lis):
    support_list = []
    for l in lis:
        for i in range(len(l)-2):    
            if l[i] != l[i+1] and l[i] == l[i+2] and [l[i],l[i+1]] not in support_list:
                support_list.append([l[i],l[i+1]])
    return support_list

f = open("day_7_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    
    inside = []
    outside = []
    while re.search("]",line):
        i_start = re.search("\[",line).end()
        i_end = re.search("]",line).start()
        inside.append(line[i_start:i_end])
        outside.append(line[:i_start-1])
        line = line[i_end+1:]
    outside.append(line)
    
    inside_aba = CheckABA(inside)
    outside_bab = CheckABA(outside)
    
    Found = False
    for p1 in inside_aba:
        for p2 in outside_bab:
            if p1[0] == p2[1] and p1[1] == p2[0]:
                total += 1
                Found = True
                break
        if Found:
            break
                    
f.close()

print(total)