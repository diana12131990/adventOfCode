import re
        
f = open("day_3_input.txt","r")
lines = []
for line in f:
    lines.append(line.strip())
f.close()

sum = 0


def isNearSymbol(c_line,num,first_check_index,last_check_index):
    c_line_index = lines.index(c_line)
    
    if first_check_index < 0:
        first_check_index = 0
    else:
        if c_line[first_check_index] != ".":
            return True        
        
    if last_check_index > len(c_line)-1:
        last_check_index = len(c_line)-1
    else:
        if c_line[last_check_index] != ".":
            return True
        
    if c_line_index > 0:
        if checkDifferentLine(lines[c_line_index-1],first_check_index,last_check_index):
            return True
        
    if c_line_index < len(lines)-1:
        if checkDifferentLine(lines[c_line_index+1],first_check_index,last_check_index):
            return True
    return False

def checkDifferentLine(line,start_index,end_index):
    for i in range(start_index,end_index+1):
        if line[i] != ".":
            return True
    return False
    

for line in lines:
    position_point = 0
    numbers_list = re.findall(r'\d+',line)
    for number in numbers_list:
        number_index = line[position_point:].find(number)+position_point
        number_length = len(number)
        
        if isNearSymbol(line,number,number_index-1,number_index+number_length):
            sum += int(number)
        position_point = number_index+number_length
        

print(sum)    