import re

def GetNextStartIndex(start_index, number):
    for i in range(start_index, len(row) - number + 1):
        # if the damage already start, skip this index
        left_index = i - 1
        if left_index > 0:
            if row[left_index] == "#":
                continue
            
        # if the left is . or ?, it could be the next start index 
        # but we need to check the end and make sure it has enough amount
        within_number = True
        for x in range(number):
            inside_index = i + x
            # if the length is less than the number, this index isn't the next start index so we should skip it
            if row[inside_index] == ".":
                within_number = False
                break
        if not within_number:
            continue
        
        # if it has enough length, we need to check if damage is longer than its length
        right_index = i + number
        if right_index < len(row):
            # if the damage isn't finish yet, skip this index
            if row[right_index] == "#":
                continue
        
        # if none of the above is reach, this index can be the next start index
        return i
    return -1
    
def CalculatePossiblility(check_index, numbers_index):
    i = check_index
    number = numbers[numbers_index]
    
    possible = 0
    # get the next start index with the number after all the following numbers possibility are found
    next_start_index = GetNextStartIndex(i, number)
    # finish after the last start index to check, which mean there is no next start index
    while next_start_index != -1:
        
        # Find all the possibility after the current number by the same function but start from the next number with next start index
        if numbers_index < len(numbers) - 1:
            next_check_index = next_start_index + number + 1
            possible += CalculatePossiblility(next_check_index, numbers_index + 1)
        # If this is the last number in the check, only one possibility now
        else:
            possible += 1
        
        # After all the possibility found with this index, we start over from the first number by moving start index one step after the next start index (because the start index need to be ".") 
        i = next_start_index + 1
        next_start_index = GetNextStartIndex(i, number)
    return possible


f = open("day_12_input.txt","r")

total_possible = 0
for line in f:
    line = line.strip()
    row,numbers = re.split(" ",line)
    numbers = re.findall(r'\d+',numbers)
    numbers = [int(x) for x in numbers]
    
    total_possible += CalculatePossiblility(0,0)
f.close()

print(total_possible)
