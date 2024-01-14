import re

f = open("day_20_input.txt","r")

numbers = [[0,4294967295]]
for line in f:
    line = line.strip()
    start,end = re.split("-",line)
    start = int(start)
    end = int(end)
    
    i = 0
    while i != len(numbers):
        r = numbers[i]
        if r[0] > end or r[1] < start:
            i += 1
        else:
            if r[0] < start:
                numbers.append([r[0],start-1])
            if r[1] > end:
                numbers.append([end+1,r[1]])
            numbers.pop(i)
f.close()

min_number = -1
for r in numbers:
    if min_number == -1 or min_number > r[0]:
        min_number = r[0]
        
print(min_number)