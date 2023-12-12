import re

def CheckPossible(springs,number):
    possible = 1
    damage_amount = springs.count("#")
    unknow_amount = springs.count("?")
    number -= damage_amount
    possible += unknow_amount- number
    return possible

def RemoveDamage(isReverse,row,numbers):
    if isReverse:
        i = -1
    else:
        i = 0
    while row[i][i] != "?":   
        isRemove = False
        if len(row[i]) > 1:
            if not isReverse:
                row[i] = row[i][1:]
            else:
                row[i] = row[i][:-1]
        else:
            row.pop(i)
            isRemove = True
            
        if numbers[i] > 1:
            numbers[i] -= 1
        else:
            numbers.pop(i)
            if not isRemove:
                if len(row[i]) > 1:
                    if not isReverse:
                        row[i] = row[i][1:]
                    else:
                        row[i] = row[i][:-1]
                else:
                    row.pop(i)
    return(row,numbers)

f = open("day_12_input.txt","r")

total_possible = 0

for line in f:
    line = line.strip()
    print(line)
    row,numbers = re.split(" ",line)
    row = row.split(".")
    while("" in row):
        row.remove("")
    
    numbers = re.findall(r'\d+',numbers)
    for x in range(len(numbers)):
        numbers[x] = int(numbers[x])
    
    possible = 1
    if len(row) == len(numbers):     # each item in list match to number
        for i in range(len(row)):
            if "?" in row[i]:
                possible *= CheckPossible(row[i],numbers[i])
    else:
        # remove the # at start and end first:
        row,numbers = RemoveDamage(False,row,numbers)
        row,numbers = RemoveDamage(True,row,numbers)  
        
        # separate numbers by row index
        numbers_group = [[]] * len(row)
        if len(row) == 1:
            numbers_group[0] = numbers
        else:
            index = 0
            for i in range(len(row)):
                num_i = 0
                remain_springs = len(row[i])
                isFinish = False
                while not isFinish:
                    if num_i + index == len(numbers):
                        isFinish = True
                    else:
                        remain_springs -= numbers[num_i + index]
                        if num_i != 0:
                            remain_springs -= 1
                        num_i += 1
                        
                        if remain_springs <= -1:
                            num_i -= 1
                            isFinish = True
                        elif remain_springs == 0:
                            isFinish = True

                numbers_group[i] = numbers[index:index+num_i]
                index += num_i
        
        # Remove springs amount equal to numbers groups total because it only one chance
        i = 0
        while i != len(row):
            springs = row[i]
            spring_amount = sum(numbers_group[i]) + len(numbers_group[i]) - 1
            if len(springs) == spring_amount:
                numbers_group.remove(numbers_group[i])
                row.remove(row[i])
                if numbers_group == []:
                    break
            else:
                # Remove known springs at start
                unknow_amount = 0
                damage_amount = 0
                runNext = False
                first_number = numbers_group[i][0]
                backLoop = False
                for x in springs:
                    if x == "?":
                        if backLoop:
                            break
                        else:
                            unknow_amount += 1
                    else:
                        damage_amount += 1
                        backLoop = True
                
                if first_number >= unknow_amount and first_number < unknow_amount+damage_amount:
                    numbers_group[i].pop(0)
                    row[i] = row[i][unknow_amount+damage_amount:]
                    if first_number == damage_amount:
                        row[i] = row[i][1:]
                    if numbers_group[i] == []:
                        numbers_group.remove(numbers_group[i])
                        row.remove(row[i])
                        i -= 1
                else:
                    # Remove know springs at end
                    unknow_amount = 0
                    damage_amount = 0
                    last_number = numbers_group[i][-1]
                    backLoop = False
                    for x in reversed(springs):
                        if x == "?":
                            if backLoop:
                                break
                            else:
                                unknow_amount += 1
                        else:
                            damage_amount += 1
                            backLoop = True
                            
                    if last_number >= unknow_amount and last_number < unknow_amount+damage_amount:
                        numbers_group[i].pop(-1)
                        row[i] = row[i][:len(row[i])-unknow_amount-damage_amount]
                        if last_number == damage_amount:
                            row[i] = row[i][:-1]
                        if numbers_group[i] == []:
                            numbers_group.remove(numbers_group[i])
                            row.remove(row[i])
                            i -= 1
                    else:
                        runNext = True
                
                if numbers_group == []:
                    break   
                if runNext:
                    i += 1
                   
        
        # Find the rest possibile        
        print(numbers_group)
        print(row)
        
    print(possible)            
    total_possible += possible
f.close()

print(total_possible)