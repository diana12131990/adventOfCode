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
        wires.update({i_module[1:]:[i_module[0],False,o_modules]})
f.close()

print(s_output)
print(wires)

def RunWire(low,high,all_high):
    low += 1    #button press
    run_wire = []
    
    # boardcaster
    for x in s_output:
        low += 1
        run_wire.append([False,x])
    
    while run_wire != []:
        name = run_wire[0][1]
        pulse = run_wire[0][0] # high = true, low = false
        if name != "output":  
            w_data = wires[name]
            if w_data[0] == "%":
                if not pulse:
                    wires[name][1] = not wires[name][1]
                    for output in wires[name][2]:
                        if wires[name][1]:
                            high += 1
                        else:
                            low += 1
                        run_wire.append([wires[name][1],output])
            else:  #w_data[0] = "&"
                wires[name][1] = pulse
                if all_high == None:
                    all_high = pulse
                    c_output = not all_high
                elif all_high and not pulse:
                    all_high = False
                    c_output = not all_high
                else:
                    c_output = not all_high
                    
                for output in wires[name][2]:
                    if c_output:
                        high += 1
                    else:
                        low += 1
                    run_wire.append([c_output,output])  
        run_wire.pop(0)      
    
    return low,high,all_high

multiply = 1
remain = 0
low = 0
high = 0
all_high = None
for i in range(1000):
    low, high, all_high = RunWire(low,high,all_high)
    continue_click = False
    for w in wires:
        if wires[w] == True:
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