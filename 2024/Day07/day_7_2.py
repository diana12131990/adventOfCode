import re
import itertools

f = open("day_7_input.txt","r")
operators = ['+', '*','||']

total = 0
line_i = 0
for line in f:
    line = line.strip()
    numbers = re.findall(r'\d+', line)
    result = int(numbers[0])
    numbers = [int(n) for n in numbers[1:]]
    line_i += 1
    print(line_i)
    op_combinations = list(itertools.product(operators, repeat=(len(numbers)-1)))
    for op_combo in op_combinations:
        value = numbers[0]
        for i, operator in enumerate(op_combo):
            if operator == '+':
                value += numbers[i+1]
            elif operator == '*':  # operator is '*'
                value *= numbers[i+1]
            else:
                string = str(value) + str(numbers[i+1])
                value = int(string)
        if value == result:
            total += result
            break
f.close()

print(total)