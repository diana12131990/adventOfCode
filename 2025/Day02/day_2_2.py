import re

f = open("day_2_input.txt","r")
ranges = f.readline().split(",")
f.close()

invaild_ID_sum = 0
for single_range in ranges:
    start, end = single_range.split("-")
    
    for num in range(int(start),int(end)+1):
        #Only check the number with at least 2 digit
        if num > 9:
            str_num = str(num)
            length = len(str_num)
            
            for sub_length in range(1, length//2 + 1):
                #Only check the length can be divine entirely
                if length % sub_length == 0:
                    pattern = str_num[:sub_length]
                    if pattern * (length // sub_length) == str_num:
                        #print(num)
                        invaild_ID_sum += num
                        break
                
print(invaild_ID_sum)