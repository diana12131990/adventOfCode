import re

f = open("day_1_input.txt","r")

left_list = []
right_list = []
for line in f:
    numbers = re.findall(r'\d+', line)
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))
f.close()

left_list.sort()
right_list.sort()

total = 0
for i in range(len(left_list)):
    if right_list[i] > left_list[i]:
        total += right_list[i] - left_list[i]
    elif left_list[i] > right_list[i]:
        total += left_list[i] - right_list[i]
print(total)