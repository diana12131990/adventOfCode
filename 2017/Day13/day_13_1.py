import re

f = open("day_13_input.txt","r")

firewall = {}
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    firewall.update({int(numbers[0]):[int(numbers[1]),1,"+"]})

severity = 0
layer_index = firewall.keys()
for i in range(max(layer_index)+1):
    if firewall.has_key(i):
        if firewall[i][1] == 1:
            severity += i * firewall[i][0]
    
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
print(severity)