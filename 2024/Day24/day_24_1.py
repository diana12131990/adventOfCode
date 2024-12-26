import re

def Gate(v1, v2, operate):
    if operate == "AND":
        return v1 & v2
    elif operate == "OR":
        return v1 | v2
    elif operate == "XOR":
        return v1 ^ v2
    
    return None

def CheckAndCalculate(k1,k2,operate):
    if k1 in values and values[k1] != -1 and k2 in values and values[k2] != -1:
        return True
    else:
        return False
        

f = open("day_24_input.txt","r")

values = {}
calculation = []
get_all_initial = False
for line in f:
    line = line.strip()
    if line == "":
        get_all_initial = True
    else:
        if get_all_initial:
            cal, result = line.split(" -> ")
            k1,operation,k2 = cal.split()
            if CheckAndCalculate(k1,k2,operation):
                values.update({result:Gate(values[k1],values[k2],operation)})
            else:
                calculation.append([k1,operation,k2,result])
                values.update({result:-1})
        else:
            key, value = line.split(": ")
            values.update({key:int(value)})
f.close()

i = 0
while calculation:
    k1,operation,k2,output = calculation[i]
    if CheckAndCalculate(k1,k2,operation):
        values[output] = Gate(values[k1],values[k2],operation)
        calculation.pop(i)
    else:
        i += 1
        
    if i == len(calculation):
        i = 0

z_result = []           
for k in values.keys():
    if k[0] == "z":
        z_result.append((re.findall(r'\d+',k),values[k]))
z_result = sorted(z_result)

result = ""
for v in reversed(z_result):
    result += str(v[1])
result = int(result, 2)
print(result)