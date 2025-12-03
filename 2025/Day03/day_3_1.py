import re

f = open("day_3_input.txt","r")

total_joltage = 0
for line in f:
    line = line.strip()
    batteries = [int(b) for b in line]
    max_digit = max(batteries)
    
    if batteries.count(max_digit) > 1:
        total_joltage += max_digit * 11
    elif batteries[-1] == max_digit:
        second_max_digit = max(batteries[:-1])
        total_joltage += second_max_digit *10 + max_digit
    else:
        max_index = batteries.index(max_digit)
        second_max_digit = max(batteries[max_index+1:])
        total_joltage += max_digit * 10 + second_max_digit
f.close()


print(total_joltage)