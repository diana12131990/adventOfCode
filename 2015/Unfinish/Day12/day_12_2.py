import re

f = open("day_12_input.txt","r")

line = f.readline()
while re.search("red",line):
    index_start = re.search("red",line).start()
    index_end = re.search("red",line).end()
    
    find_start = False
    find_end = False
    step_back = 1
    step_forward = 0
    additional_big_circle = 0
    left_in_middle_circle = False
    right_in_middle_circle = True
    while not find_start or not find_end:
        # print(line[index_start - step_back:index_end+step_forward+1])
        if not find_start:
            index = index_start - step_back
            if line[index] == "[":
                if left_in_middle_circle:
                    left_in_middle_circle = False
                elif not find_end:
                    in_middle_circle = True
                    additional_middle_circle = 0
                    while in_middle_circle:
                        if line[index_end + step_forward] == "[":
                            additional_middle_circle += 1
                            
                        if line[index_end + step_forward] == "]":
                            if additional_middle_circle != 0:
                                additional_middle_circle -= 1
                            else:
                                in_middle_circle = False
                        step_forward += 1
                        # print(line[index_start - step_back:index_end+step_forward+1])
                step_back += 1
            elif line[index] == "]":
                left_in_middle_circle = True
                step_back += 1
            elif line[index] == "}":
                additional_big_circle += 1
                step_back += 1
            elif line[index] == "{":
                if additional_big_circle != 0:
                    additional_big_circle -= 1
                    step_back += 1
                else:
                    find_start = True
            else:
                step_back += 1
            # print(line[index_start - step_back:index_end+step_forward+1])
                
        if not find_end:
            index = index_end + step_forward
            if line[index] == "]" and not find_start:
                in_middle_circle = True
                additional_middle_circle = 0
                while in_middle_circle:
                    if line[index_start - step_back] == "]":
                        additional_middle_circle += 1  
                        
                    if line[index_start - step_back] == "[":
                        if additional_middle_circle != 0:
                            additional_middle_circle -= 1
                        else:
                            in_middle_circle = False
                    print(line[index_start - step_back:index_end+step_forward+1])
                    step_back += 1       
                step_forward += 1
            elif line[index] == "]":
                right_in_middle_circle = True
                step_forward += 1            
            elif line[index] == "{":
                additional_big_circle += 1
                step_forward += 1         
            elif line[index] == "}":
                if additional_big_circle != 0:
                    additional_big_circle -= 1  
                    step_forward += 1
                else:
                    find_end = True
            else:
                step_forward += 1
    print(line[index_start - step_back:index_end+step_forward+1])    
    index_start -= step_back
    index_end += step_forward
    # print(line[index_start-10:index_start])
    # print(line[index_end+1:index_end+10])
    line = line[:index_start] + line[index_end+1:]
    print(line)
    # print(line[index_start-10:index_end+10])

result = [int(d) for d in re.findall(r'-?\d+', line)]
total_count = sum(result)
f.close()
print(total_count)