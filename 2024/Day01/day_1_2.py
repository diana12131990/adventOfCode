import re

f = open("day_1_input.txt","r")

left_list = []
right_list = []
for line in f:
    numbers = re.findall(r'\d+', line)
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))
f.close()

total = 0
for n in left_list:
    total += n*right_list.count(n)
print(total)