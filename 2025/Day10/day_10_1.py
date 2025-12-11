
import re

f = open("day_10_input.txt","r")

total_min_press = 0

for line in f:
    line = line.strip()
    part_1,part_2 = line.split("{")
    diagram, buttons = part_1.split("]")
    diagram = [1 if c == '#' else 0 for c in diagram[1:]]
    
    buttons = buttons.split("(")
    button_sch = []
    for b in buttons:
        lights_switch = tuple(map(int, re.findall(r'\d+', b)))
        if lights_switch:
            button_sch.append(lights_switch)
    
    light_amount = len(diagram)
    button_amount = len(button_sch)
    min_presses = float('inf')
    
    # Each button can only click once or never get click
    for b in range(1 << button_amount): # 2**button_amount combination
        current_presses = 0
        current_state = [0] * light_amount # Initially all lights are off

        # Check each button based on the current combination 'b'
        for j in range(button_amount):
            if (b >> j) & 1:  # If the j-th bit is set, this button is "pressed"
                current_presses += 1
                for i in button_sch[j]:
                    current_state[i] ^= 1 # Toggle the light

        if current_state == diagram:
            min_presses = min(min_presses, current_presses)   
    
    total_min_press += min_presses
    
f.close()

print(total_min_press)