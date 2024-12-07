import re

f = open("day_3_input.txt","r")

total = 0
for line in f:
    mul_numbers = re.findall(r"mul\((\d+),(\d+)\)", line)
    for numbers in mul_numbers:
        total += int(numbers[0])*int(numbers[1])
f.close()

print(total)