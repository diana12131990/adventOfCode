import re

f = open("day_20_input.txt","r")

s_output = []
wires = {}

for line in f:
    line = line.strip()
    i_module, o_modules = re.split(" -> ",line)
    if re.search(",",o_modules):
        o_modules = re.split(", ",o_modules)
    else:
        o_modules = [o_modules]
        
    if i_module == "broadcaster":
        s_output = o_modules
    else:
        if i_module[0] == "%":
            wires.update({i_module[1:]:[i_module[0],False,o_modules]})
        else:
            wires.update({i_module[1:]:[i_module[0],{},o_modules]})
f.close()

for name in wires:
    if wires[name][0] == "&":
        for w in s_output:
            if w == name:
                wires[name][1].update({"broadcaster":False})
        for w in wires:
            if w != name:
                if name in wires[w][2]:
                    wires[name][1].update({w:False})

def RunWire(low,high):
    low += 1    #button press
    run_wire = []
    
    # boardcaster
    for x in s_output:
        low += 1
        run_wire.append(["broadcaster",False,x])
    
    while run_wire != []:
        sender = run_wire[0][0]
        pulse = run_wire[0][1] # high = true, low = false
        name = run_wire[0][2]
        if wires.has_key(name):  
            w_data = wires[name]
            if w_data[0] == "%":
                if not pulse:
                    wires[name][1] = not wires[name][1]
                    for output in wires[name][2]:
                        if wires[name][1]:
                            high += 1
                        else:
                            low += 1
                        run_wire.append([name,wires[name][1],output])
            else:  #w_data[0] = "&"
                wires[name][1][sender] = pulse
                if False in wires[name][1].values():
                    c_output = True
                else:
                    c_output = False
                    
                for output in wires[name][2]:
                    if c_output:
                        high += 1
                    else:
                        low += 1
                    run_wire.append([name,c_output,output])  
        run_wire.pop(0)      
    
    return low,high

multiply = 1
remain = 0
low = 0
high = 0
for i in range(1000):
    low, high = RunWire(low,high)
    continue_click = False
    for w in wires:
        if wires[w][0] == "%":
            if wires[w][1] == True:
                continue_click = True
                break
        else:
            if True in wires[w][1].values():
                continue_click = True
                break                
    if not continue_click:
        multiply = 1000/(i+1)
        remain = 1000%(i+1)
        break

low *= multiply
high *= multiply

if remain != 0:
    for i in range(remain):
        RunWire(low,high)
        

print(low * high)