import re

f = open("day_3_input.txt","r")

total = 0
ignore_following = False
for line in f:
    for instruction in re.split(r'(don\'t\(\)|do\(\))', line):
        if instruction == 'don\'t()':
            ignore_following = True
        elif instruction == 'do()':
            ignore_following = False
        else:
            if not ignore_following:
                mul_numbers = re.findall(r"mul\((\d+),(\d+)\)", instruction)
                for numbers in mul_numbers:
                    total += int(numbers[0])*int(numbers[1])                
f.close()

print(total)