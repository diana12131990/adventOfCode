import re

f = open("day_16_input.txt","r")

tape = {
    "children": "3",
    "cats": "7",
    "samoyeds": "2",
    "pomeranians": "3",
    "akitas": "0",
    "vizslas": "0",
    "goldfish": "5",
    "trees": "3",
    "cars": "2",
    "perfumes": "1",   
}

aunt = 1
for line in f:
    line = line.strip()
    index = re.search(": ",line).end()
    line = re.split(", ",line[index:])
    
    skip = False
    for x in line:
        name, number = re.split(": ",x)
        if tape[name] != number:
            skip = True
            break
    if not skip:
        print(aunt)
        break
    aunt += 1
f.close()