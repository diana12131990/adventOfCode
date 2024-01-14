import re

string = "fbgdceah"
string = [x for x in string]

f = open("day_21_input.txt","r")
instruction = []

for line in f:
    line = line.strip()
    instruction.append(line)
f.close()

for line in reversed(instruction):
    if "swap" in line:
        
        if "position" in line:
            numbers = re.findall("\d+",line)
            i = int(numbers[0])
            j = int(numbers[1])
            char = string[i]
            string[i] = string[j]
            string[j] = char
            
        elif "letter" in line:
            line = line.replace("swap ","")
            line = line.replace("letter ","")
            start,end = re.split(" with ",line)
            for i in range(len(string)):
                if string[i] == start:
                    string[i] = end
                elif string[i] == end:
                    string[i] = start
                    
    elif "rotate" in line:
        step = 0
        
        if "position" in line:
            char = line[-1]
            for i in range(len(string)):
                if string[i] == char:
                    step = i
                    break
            if step == 0 or step >= 7:
                step += 1
            else:
                step -= 1
            step *= -1                
        
        else:
            n = re.findall("\d+",line)
            step = int(n[0])
            if "Right" in line:
                step *= -1
        
        new_string = [""]*len(string)
        for i in range(len(string)):
            j = i + step
            if j >= len(string):
                j %= len(string)
            elif j < 0:
                j += len(string)
            new_string[j] = string[i]
        string = []
        for x in new_string:
            string.append(x)
        
    elif "reverse" in line:
        numbers = re.findall("\d+",line)
        start = int(numbers[0])
        end = int(numbers[1])
        new_string = []
        for i in range(start):
            new_string.append(string[i])
        for i in reversed(range(start,end+1)):
            new_string.append(string[i])
        for i in range(end+1,len(string)):
            new_string.append(string[i])
        string = []
        for x in new_string:
            string.append(x)        
            
    elif "move" in line:
        numbers = re.findall("\d+",line)
        start = int(numbers[0])
        end = int(numbers[1])
        char = string[end]
        string.pop(end)
        string.insert(start,char)


print("".join(string))