import re

password = "fbgdceah"
password = list(password)

with open('day_21_input.txt', 'r') as file:
    lines = file.readlines()

for instruction in reversed(lines):
    inst = instruction.split()
    if 'swap position' in instruction:
        x, y = int(inst[2]), int(inst[5])
        password[x], password[y] = password[y], password[x]
    elif 'swap letter' in instruction:
        x, y = password.index(inst[2]), password.index(inst[5])
        password[x], password[y] = password[y], password[x]
    elif 'rotate based' in instruction:
        i = password.index(inst[-1])
        if i % 2 == 0:
            rotation = (i + 2) / 2 if i != 0 else 9
        else:
            rotation = i / 2 + 1
        rotation = int(rotation % len(password))
        password = password[rotation:] + password[:rotation]
    elif 'rotate' in instruction:
        steps = int(inst[2])
        if 'left' in inst[1]:
            password = password[-steps:] + password[:-steps]
        else:
            password = password[steps:] + password[:-steps]
    elif 'reverse positions' in instruction:
        x, y = int(inst[2]), int(inst[4])
        password = password[:x] + password[x:y+1][::-1] + password[y+1:]
    elif 'move' in instruction:
        x = int(inst[2])
        y = int(inst[5])
        letter = password.pop(x)
        password.insert(y, letter)

print("".join(password))