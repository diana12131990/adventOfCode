import re

f = open("day_9_input.txt","r")

total = 0
line = f.readline()
line = line.strip()
brackets = re.findall(r'\(.*?\)', line)
while brackets != []:
    total += re.search(brackets[0],line).start()-1
    num = re.findall("\d+",brackets[0])
    total += int(num[0])*int(num[1])
    line = line[re.search(brackets[0],line).end()+1+int(num[0]):]
    brackets = re.findall(r'\(.*?\)', line)
total += len(line)
f.close()

print(total)