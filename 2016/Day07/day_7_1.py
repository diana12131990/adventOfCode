import re

def IsABBA(line):
    return line[0] != line[1] and line[0] == line[3] and line[1] == line[2]
        

f = open("day_7_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    
    inside = []
    outside = []
    while re.search("]",line):
        i_start = re.search("\[",line).end()
        i_end = re.search("]",line).start()
        inside.append(line[i_start:i_end])
        outside.append(line[:i_start-1])
        line = line[i_end+1:]
    outside.append(line)
    
    skip = False
    for line in inside:
        for i in range(len(line)-3):
            if IsABBA(line[i:i+4]):
                skip = True
                break
        if skip:
            break
        
    if not skip:
        for line in outside:
            Found = False
            for i in range(len(line)-3):
                if IsABBA(line[i:i+4]):
                    total += 1
                    Found = True
                    break
            if Found:
                break
f.close()

print(total)