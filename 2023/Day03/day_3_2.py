import re

f = open("day_3_input.txt","r")
lines = []
for temp_line in f:
    lines.append(temp_line.strip())
f.close()

sum = 0

def CheckDifferentLine(line,g_pos,num_1,num_2):
    if line[g_pos].isdigit():
        check_end_pos = g_pos
        while line[check_end_pos+1].isdigit():
            check_end_pos+=1
        num_1,num_2 = DefineNum(line,check_end_pos,num_1,num_2) 
    else:
        num_1,num_2 = CheckSide(line,g_pos,num_1,num_2) 
        
    return num_1,num_2

def CheckSide(line,g_pos,num_1,num_2):
    start_pos = g_pos-1
    end_pos = g_pos+1
    
    if start_pos >=0:
        if line[start_pos].isdigit():
            num_1,num_2 = DefineNum(line,start_pos,num_1,num_2)
    if end_pos <= len(line)-1:
        if line[end_pos].isdigit():
            num_1,num_2 = DefineNum(line,end_pos,num_1,num_2)    
            
    return num_1,num_2


def DefineNum(line,pos,num_1,num_2):
    if num_1 != 0:
        num_2 = GetNumber(line,pos)
    else:
        num_1 = GetNumber(line,pos)
    return num_1,num_2


def GetNumber(line,digit_pos):
    position_point = 0
    numbers_list = re.findall(r'\d+',line)
    for number in numbers_list:
        number_index = line[position_point:].find(number)+position_point
        number_length = len(number) 
        if number_index == digit_pos or number_index+number_length-1 == digit_pos:
            return number
        position_point = number_index+number_length



for c_line in lines:
    gear_indexes = [x.start() for x in re.finditer('\*', c_line)]
    for gear_pos in gear_indexes:
        c_line_index = lines.index(c_line)
        num_1 = 0
        num_2 = 0
            
        num_1,num_2 = CheckSide(c_line,gear_pos,num_1,num_2)
            
        if c_line_index > 0:
            l_line = lines[c_line_index-1]
            num_1,num_2 = CheckDifferentLine(l_line,gear_pos,num_1,num_2)
                            
        if c_line_index < len(lines)-1:
            n_line = lines[c_line_index+1]
            num_1,num_2 = CheckDifferentLine(n_line,gear_pos,num_1,num_2)        
        
        if num_1 != 0 and num_2 != 0:
            sum += int(num_1)*int(num_2)
        

print(sum)    
