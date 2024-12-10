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

def getSecond(c):
    return ord(c) - ord('A') + 61

finish_order = ""
start_step = []
total_second = -1
queue_step = []
while wait_steps or queue_step or start_step:
    # Countdown
    total_second += 1
    for si in range(len(start_step)):
        start_step[si][1] -= 1     
    
    # set the step to finish first and remove it from conditional
    si = 0
    while si < len(start_step):
        if start_step[si][1] == 0:
            s = start_step[si][0]
            start_step.pop(si)
            finish_order += s
            for key, value in conditionals.items():
                if s in value:
                    conditionals[key].remove(s)            
        else:
            si += 1    
    keys = list(conditionals.keys())
    for k in keys:
        if not conditionals[k]:
            del conditionals[k]    
            
    # move step to queue step for them to be ready to start
    i = 0
    while i < len(wait_steps):
        s = wait_steps[i]
        if s not in conditionals:
            queue_step.append(s)
            wait_steps.remove(s)   
        else:
            i+=1

    # check if any step can start
    while len(start_step) < 4 and queue_step:
        queue_step = sorted(queue_step)
        s = queue_step[0]
        start_step.append([s,getSecond(s)])
        queue_step.pop(0)
    
print(total_second)