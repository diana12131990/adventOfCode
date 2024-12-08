import re
import itertools

f = open("day_7_input.txt","r")
operators = ['+', '*']

total = 0
for line in f:
    line = line.strip()
    numbers = re.findall(r'\d+', line)
    result = int(numbers[0])
    numbers = [int(n) for n in numbers[1:]]
    
    op_combinations = list(itertools.product(operators, repeat=(len(numbers)-1)))
    for op_combo in op_combinations:
        value = numbers[0]
        for i, operator in enumerate(op_combo):
            if operator == '+':
                value += numbers[i+1]
            else:  # operator is '*'
                value *= numbers[i+1]
        if value == result:
            total += result
            break
f.close()

print(total)