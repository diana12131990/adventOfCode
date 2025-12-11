
import re
import collections

f = open("day_10_input.txt","r")

total_min_press = 0
for line in f:
    line = line.strip()
    part_1,part_2 = line.split("{")
    diagram, buttons = part_1.split("]")
    
    buttons = buttons.split("(")
    button_sch = []
    for b in buttons:
        lights_switch = list(map(int, re.findall(r'\d+', b)))
        if lights_switch:
            button_sch.append(lights_switch)
    
    joltage_target = tuple(map(int, re.findall(r'\d+', part_2)))
    
    counters_amount= len(joltage_target)
    button_amount = len(button_sch)

    # Use tuple for hashable state in BFS
    initial_joltage_tuple = tuple([0] * counters_amount)
    
    # BFS queue: stores (current_joltage_levels_tuple, total_presses)
    queue = collections.deque([(initial_joltage_tuple, 0)])

    # Dictionary to store the minimum presses to reach a certain joltage state
    # { joltage_tuple: min_presses }
    min_presses_to_state = {initial_joltage_tuple: 0}
    min_presses = float('inf')

    while queue:
        current_joltage, presses = queue.popleft()

        # If we've reached the target, update the minimum and continue
        if current_joltage == joltage_target:
            min_presses = min(min_presses, presses)
            continue
        
        # If current presses already exceed the best found so far for the target, prune
        if presses >= min_presses:
            continue        

        # Try pressing each button once
        for j in range(button_amount):
            new_joltage = list(current_joltage)
            for i in button_sch[j]:
                new_joltage[i] += 1
            
            new_joltage = tuple(new_joltage)
            new_presses = presses + 1

            # Check if this new state is valid (not exceeding target for any counter)
            is_valid_state = True
            for i in range(counters_amount):
                if new_joltage[i] > joltage_target[i]:
                    is_valid_state = False
                    break
            
            if not is_valid_state:
                continue

            # If we haven't visited this state, or found a shorter path to it
            if new_joltage not in min_presses_to_state or new_presses < min_presses_to_state[new_joltage]:
                min_presses_to_state[new_joltage] = new_presses
                queue.append((new_joltage, new_presses))  
    
    total_min_press += min_presses
f.close()

print(total_min_press)