import re

f = open("day_8_input.txt","r")

values = {}
max_value = 0
for line in f:
    line = line.strip()
    statement,condition = re.split(" if ",line)
    statement = statement.split()
    condition = condition.split()
    
    if not values.has_key(statement[0]):
        values.update({statement[0]:0})
    if not values.has_key(condition[0]):
        values.update({condition[0]:0})
    if not re.search("\d",statement[2]):
        if not values.has_key(statement[2]):
            values.update({statement[2]:0})
    if not re.search("\d",condition[2]):
        if not values.has_key(condition[2]):
            values.update({condition[2]:0})
    
    # CheckCondition
    ConditionState = False
    a = values[condition[0]]
    b = 0
    if re.search("\d",condition[2]):
        b = int(condition[2])
    else:
        b = values[condition[2]]
    
    if condition[1] == "==":
        if a == b:
            ConditionState = True
    elif condition[1] == "!=":
        if a != b:
            ConditionState = True
    elif condition[1] == ">=":
        if a >= b:
            ConditionState = True
    elif condition[1] == "<=":
        if a <= b:
            ConditionState = True
    elif condition[1] == ">":
        if a > b:
            ConditionState = True
    elif condition[1] == "<":
        if a < b:
            ConditionState = True      
    
    # Run Statement if Condition is True
    if ConditionState:
        x = values[statement[0]]
        y = 0
        result = 0
        
        if re.search("\d",statement[2]):
            y = int(statement[2])
        else:
            y = values[statement[2]]
            
        if statement[1] == "inc":
            result = x + y
        elif statement[1] == "dec":
            result = x - y
        values.update({statement[0]:result})
                
    if max_value < max(values.values()):
        max_value = max(values.values())
    
f.close()

print(max_value)