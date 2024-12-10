import re

f = open("day_7_input.txt","r")

conditionals = {}
wait_steps = []
for line in f:
    steps = re.findall(r'step\s(\w)', line, re.IGNORECASE) 
    if steps[1] in conditionals:
        conditionals[steps[1]].append(steps[0])
    else:
        conditionals.setdefault(steps[1], []).append(steps[0])
    
    for s in steps:
        if s not in wait_steps:
            wait_steps.append(s)
f.close()

start_order = ""
queue_step = []
while wait_steps or queue_step:
    i = 0
    while i < len(wait_steps):
        s = wait_steps[i]
        if s not in conditionals:
            queue_step.append(s)
            wait_steps.remove(s)   
        else:
            i+=1
    queue_step = sorted(queue_step)
    s = queue_step[0]
    start_order += queue_step[0]
    queue_step.pop(0)
    for key, value in conditionals.items():
        if s in value:
            conditionals[key].remove(s)    
    
    keys = list(conditionals.keys())
    for k in keys:
        if not conditionals[k]:
            del conditionals[k]

print(start_order)