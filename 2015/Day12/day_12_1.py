import re

f = open("day_12_input.txt","r")

line = f.readline()
result = [int(d) for d in re.findall(r'-?\d+', line)]
total_count = sum(result)
f.close()
print(total_count)