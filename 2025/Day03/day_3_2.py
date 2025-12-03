import re

f = open("day_3_input.txt","r")

total_joltage = 0
for line in f:
    line = line.strip()
    batteries = [int(b) for b in line]
    chosen_batteries = []
    start_i = 0
    
    for n in range(12):
        
        # We need enough remaining digits (12-(n+1)) in batteries after picking the current battery at index 'i'
        # (len(batteries)-1)-i >= (12-(n+1))
        # i <= (len(batteries)-1) - (12-(n+1))
        # i <= (len(batteries)-1) - (12-n-1)
        # i <= len(batteries)-1-12+n+1
        # i <= len(batteries)-12+n
        end_i = len(batteries)-12+n
        
        max_digit = max(batteries[start_i:end_i+1])
        max_digit_index = batteries.index(max_digit, start_i,end_i+1)
        
        chosen_batteries.append(str(max_digit))
        start_i = max_digit_index+1
        
    max_bank_joltage = "".join(chosen_batteries)
    #print(max_bank_joltage)
    total_joltage += int(max_bank_joltage)    
f.close()

print(total_joltage)