import re

f = open("day_13_input.txt","r")

firewall = {}

for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    firewall.update({int(numbers[0]):[int(numbers[1]),1,"+"]})
    
layer_index = firewall.keys()


def Move():
    for x in layer_index:
        layer_amount = firewall[x][0]
        step = firewall[x][1]
        direction = firewall[x][2]
        
        if direction == "+":
            if step == layer_amount:
                step -= 1
                direction = "-"
            else:
                step += 1
        elif direction == "-":
            if step == 1:
                step += 1
                direction = "+"
            else:
                step -= 1
        firewall.update({x:[layer_amount,step,direction]})    

delay = 81725
HasSeverity = True

while HasSeverity:
    if delay != 0:
        for t in range(delay):
            Move()
    Interrupt = False
    for i in range(max(layer_index)+1):
        if firewall.has_key(i):
            if firewall[i][1] == 1:
                delay += 1
                Interrupt = True
                for x in layer_index:
                    layer_amount = firewall[x][0]
                    firewall.update({x:[layer_amount,1,"+"]})
                    break
        Move()
    if not Interrupt:
        HasSeverity = False

print(delay+1)