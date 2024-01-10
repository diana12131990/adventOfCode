import re

f = open("day_9_input.txt","r")

total = 0
line = f.readline()
line = line.strip()
brackets = re.findall(r'\(.*?\)', line)
while brackets != []:
    i = 0
    total += re.search(brackets[i],line).start()-1
    while line[re.search(brackets[i],line).end()+1] == "(":
        i += 1
    num = re.findall("\d+",brackets[i])
    digit_amount = int(num[0])
    count = digit_amount*int(num[1])
    for x in range(i):
        inner_num = re.findall("\d+",brackets[x])
        count *= int(inner_num[1])
    total += count
    
    line = line[re.search(brackets[i],line).end()+1+digit_amount:]
    brackets = re.findall(r'\(.*?\)', line)
total += len(line)
f.close()

print(total)