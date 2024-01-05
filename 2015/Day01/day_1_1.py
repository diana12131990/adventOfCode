import re

f = open("day_1_input.txt","r")

line = f.readline()
f.close()

up = line.count("(")
down = line.count(")")
floor = up - down
print(floor)