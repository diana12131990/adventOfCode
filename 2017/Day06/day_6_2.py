import re

f = open("day_6_input.txt","r")

line = f.readline()
line = line.strip()
line = line.split()
values = [int(x) for x in line]
f.close()

results = []
results.append(values)
digits = len(values)
InLoop = False
time = 0

while not InLoop:
    time += 1
    values = results[-1]
    max_value = max(values)
    max_i = values.index(max_value)
    spread_amount = max_value/digits
    remain = max_value%digits
    
    new_value = []
    for i in range(digits):
        if i == max_i:
            new_value.append(spread_amount)
        else:
            new_value.append(values[i] + spread_amount)
    
    i = max_i + 1        
    while remain > 0:
        if i == digits:
            i = 0
        new_value[i] += 1
        i += 1
        remain -= 1
    
    if new_value in results:
        first_i = results.index(new_value)
        print(time - first_i)
        InLoop = True
    else:
        results.append(new_value)
