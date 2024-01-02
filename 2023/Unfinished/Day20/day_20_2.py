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

def DetectWires():
    for x in detect_w:
        if not detect_w[x][2]:
            return False
    return True

def RunWire():
    run_wire = []
    # boardcaster
    for x in s_output:
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
                    if name == rx_s_name:
                        if not wires[name][1]:
                            return True
                        else:
                            print(wires[name][1])
                    for output in wires[name][2]:
                        run_wire.append([name,wires[name][1],output])
            else:  #w_data[0] = "&"
                wires[name][1][sender] = pulse
                if False in wires[name][1].values():
                    c_output = True
                else:
                    c_output = False
                if name == rx_s_name:
                    if not c_output:
                        return True 
                    else:
                        print(wires[name][1])                
                for output in wires[name][2]:
                    run_wire.append([name,c_output,output])  
        run_wire.pop(0)      
    
    return False

for w in wires:
    if "rx" in wires[w][2]:
        rx_s_name = w
        break

click_time = 0
has_low = False
while not has_low:
    click_time+=1
    has_low = RunWire()
    print(click_time)

print(click_time)