
import re

f = open("day_6_input.txt","r")

worksheet = []

for line in f:
    line = line.strip()
    line = line.split()
    worksheet.append(line)
f.close()

operators = worksheet.pop()
total = 0

for i,op in enumerate(operators):
    current_ans = 0
    if op == "*":
        current_ans = 1
    for line in worksheet:
        if op == "*":
            current_ans *= int(line[i])
        elif op == "+":
            current_ans += int(line[i])
    total += current_ans
    
print(total)