import re

f = open("day_12_input.txt","r")

line = f.readline()
brackets = re.findall(r'\[.*?\]', line)
for x in brackets:
    print(x)
    end_i = re.search(x,line).start()
    print(line[end_i+1])

result = [int(d) for d in re.findall(r'-?\d+', line)]
total_count = sum(result)
f.close()
print(total_count)