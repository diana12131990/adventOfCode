import re

def GetValue(parent):
    child_value = []
    for x in instruction[parent]:
        root_value = values[x]
        if instruction.has_key(x):
            root_value += GetValue(x)
        child_value.append(root_value)
    
    diff_i = -1
    normal_i = 0
    for n in child_value:
        if child_value.count(n) == 1:
            diff_i = child_value.index(n)
            break
    if diff_i == 0:
        normal_i = 1
    if diff_i != -1:
        diff = child_value[normal_i]-child_value[diff_i]
        original_value = values[instruction[parent][diff_i]]
        print(original_value + diff)
            
    return child_value[normal_i]*len(child_value)



f = open("day_7_input.txt","r")

instruction = {}
values = {}
for line in f:
    line = line.strip()
    if "->" in line:
        front, back = re.split(" -> ",line)
        name, value = re.split(" ",front)
        children = back.split(", ")
        instruction.update({name:children})
    else:
        name, value = re.split(" ",line)
    num = re.findall("\d+",value)
    values.update({name:int(num[0])})
f.close()


# Find root
start_name = ""
for name in instruction:
    Skip = False
    for check in instruction:
        if check != name:
            if name in instruction[check]:
                Skip = True
                break
    if not Skip:
        start_name = name
        break

total = []
for name in instruction[start_name]:
    value = values[name]
    value += GetValue(name)
    total.append(value)