import re

f = open("day_7_input.txt","r")

operators = ["AND","OR","LSHIFT","RSHIFT","NOT"]

wires = {}
unknow_wires = []

for line in f:
    line = line.strip()
    
    signal, wire = re.split(" -> ",line)
    
    need_operation = False
    op = ""
    for x in operators:
        if x in signal:
            op = x
            need_operation = True
            break
    if not need_operation and re.search("\d",signal):
        if wire == "b":
            wires.update({wire:3176})
        else:
            wires.update({wire:int(signal)})
    else:
        unknow_wires.append([wire,op,signal])
        
f.close()


while unknow_wires != []:
    wire = unknow_wires[0][0]
    op = unknow_wires[0][1]
    signal = unknow_wires[0][2]
    
    if op == "":
        if wires.has_key(signal):
            wires.update({wire:wires[signal]})
        else:
            unknow_wires.append([wire,op,signal])
    elif op == "NOT":
        _,x = re.split("NOT ",signal)
        if re.search("\d",x):
            wires.update({wire:~int(x)})
        elif wires.has_key(x):
            wires.update({wire:~wires[x]&0xffff})
        else:
            unknow_wires.append([wire,op,signal])
    else:
        skip = False
        x,y = re.split(" "+op+" ",signal)
        
        if re.search("\d",x):
            x = int(x)
        elif wires.has_key(x):
            x = wires[x]
        else:
            skip = True
        
        if re.search("\d",y):
            y = int(y)
        elif wires.has_key(y):
            y = wires[y]
        else:
            skip = True
            
        if skip:
            unknow_wires.append([wire,op,signal])
        else:
            if op == "AND":
                wires.update({wire:x&y})
            elif op == "OR":
                wires.update({wire:x|y})
            elif op == "LSHIFT":
                wires.update({wire:x<<y})
            elif op == "RSHIFT":
                wires.update({wire:x>>y})
    unknow_wires.pop(0)
                
print(wires["a"])