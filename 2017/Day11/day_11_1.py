import re

f = open("day_11_input.txt","r")

line = f.readline()
line = line.strip()
direction = line.split(",")
print(direction)

x = 0.0
y = 0.0

for d in direction:
    if d == "n":
        x += 1
    elif d == "s":
        x -= 1
    elif d == "e":
        y += 1
    elif d == "w":
        y -= 1
    elif d == "ne":
        x += 0.5
        y += 0.5
    elif d == "se":
        x += 0.5
        y -= 0.5
    elif d == "nw":
        x -= 0.5
        y += 0.5
    elif d == "sw":
        x -= 0.5
        y -= 0.5

print(int(abs(x)+abs(y)))