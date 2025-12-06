
import re
import math

f = open("day_6_input.txt","r")

file = []
for line in f:
    file.append(line)
f.close()

operators = file.pop()
experssion_num_amount = len(file)

# Get the indice for operators in the line so we know how to cut the string for the numbers later
start_indice = [i for i, char in enumerate(operators) if char != " "]
operators = operators.split()

# Cutting the number, but keep them in string type since we still need to spaces
worksheet = []
for line in file:
    
    new_list = []
    for i in range(len(start_indice)-1):
        new_list.append(line[start_indice[i]:start_indice[i+1]])
    new_list.append(line[start_indice[-1]:-1])
    
    worksheet.append(new_list)



total = 0
for i,op in enumerate(operators):
    
    # Save all the numbers for this operator in a list first
    current_nums = []
    for x in range(len(worksheet[0][i])):
        
        # Get the digit from each line and combine into a string first
        current_num = ""
        for n in range(experssion_num_amount):
            current_num += worksheet[n][i][x]
        
        if current_num.strip():
            current_nums.append(int(current_num))
        
    if op == "*":
        total += math.prod(current_nums)
    elif op == "+":
        total += sum(current_nums)
    
print(total)