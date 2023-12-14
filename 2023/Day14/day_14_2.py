import re

f = open("day_14_input.txt","r")

def DoCycle(mirror):
    # North
    for i in range(len(mirror)-1):
        i+=1
        for j in range(len(mirror[0])):
            if mirror[i][j] == "O":
                row = i-1
                while row >= 0:
                    if mirror[row][j] == "O" or mirror[row][j] == "#":
                        row += 1
                        break
                    else:
                        if row == 0:
                            break
                        row -= 1
                if row != i:
                    mirror[row][j] = "O"
                    mirror[i][j] = "."
    #West
    for i in range(len(mirror)):
        for j in range(len(mirror[0])-1):
            j+=1
            if mirror[i][j] == "O":
                column = j-1
                while column >= 0:
                    if mirror[i][column] == "O" or mirror[i][column] == "#":
                        column+=1
                        break
                    else:
                        if column == 0:
                            break
                        column -= 1
                if column != j:
                    mirror[i][column] = "O"
                    mirror[i][j] = "."
    #South
    for i in reversed(range(len(mirror)-1)):
        for j in range(len(mirror[0])):
            if mirror[i][j] == "O":
                row = i+1
                while row <= len(mirror) - 1:
                    if mirror[row][j] == "O" or mirror[row][j] == "#":
                        row -= 1
                        break
                    else:
                        if row == len(mirror) - 1:
                            break
                        row += 1
                if row != i:
                    mirror[row][j] = "O"
                    mirror[i][j] = "."
    #East
    for i in range(len(mirror)):    
        for j in reversed(range(len(mirror[0])-1)):
            if mirror[i][j] == "O":
                column = j+1
                while column <= len(mirror[0]) - 1:
                    if mirror[i][column] == "O" or mirror[i][column] == "#":
                        column-=1
                        break
                    else:
                        if column == len(mirror[0]) - 1:
                            break
                        column+= 1
                if column != j:
                    mirror[i][column] = "O"
                    mirror[i][j] = "."        
    return mirror


mirror = []

for line in f:
    line = line.strip()
    line = [x for x in line]
    mirror.append(line)

# Do cycle 1000000000 times but stop if we find the loop list

load_sum_list = []
remain_cycle_amount = 0
loop_list = []

for i in range(10000):
    load_sum = 0
    mirror = DoCycle(mirror)
    for x in range(len(mirror)):
        load_amount = len(mirror) - x
        total_rock = mirror[x].count("O")
        load_sum += load_amount * total_rock

    load_sum_list.append(load_sum)
    
    if i != 0 and i%100 == 0:
        first_i = (i/100-1)*100
        Last_i = -1
        check_num = load_sum_list[first_i]
        if check_num in load_sum_list[first_i+1:]:
            CheckLoop = True
            index = load_sum_list.index(check_num)+1
            check_i = first_i + 1
            while index < len(load_sum_list) and check_i < len(load_sum_list):
                if load_sum_list[index] != load_sum_list[check_i]:
                    # Not find loop, continue the main loop
                    CheckLoop = False
                    break
                else:
                    if load_sum_list[first_i] == load_sum_list[check_i]:
                        inLoop = True
                        for x in range(10):
                            if check_i+x >= len(load_sum_list) or load_sum_list[first_i+x] != load_sum_list[check_i+x]:
                                inLoop = False
                                break
                        if inLoop:
                            Last_i = check_i
                            break
                    index += 1
                    check_i += 1
            
            if CheckLoop:
                remain_cycle_amount = 1000000000 - Last_i
                loop_list = load_sum_list[first_i:Last_i]
                break

index = remain_cycle_amount%len(loop_list)-1
print(loop_list[index])

f.close()