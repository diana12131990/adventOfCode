import re

def GetPin(strings):
    pin = []
    for i in range(5):
        amount = 0
        for line in strings:
            if line[i] == "#":
                amount += 1
        pin.append(amount)
    return pin

f = open("day_25_input.txt","r")

strings = []
keys = []
locks = []
for line in f:
    line = line.strip()
    if line:
        strings.append(line)
    else:
        if "#" in strings[0]:
            locks.append(GetPin(strings[1:-1]))
        else:
            keys.append(GetPin(strings[1:-1]))
        
        strings.clear()
f.close()

if "#" in strings[0]:
    locks.append(GetPin(strings[1:-1]))
else:
    keys.append(GetPin(strings[1:-1]))

fit_amount = 0
for key in keys:
    for lock in locks:
        overlap = False
        for i in range(len(key)):
            if key[i]+lock[i] > 5:
                overlap = True
                break
        if not overlap:
            fit_amount += 1
print(fit_amount)