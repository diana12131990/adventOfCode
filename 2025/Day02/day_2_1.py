import re

f = open("day_2_input.txt","r")
ranges = f.readline().split(",")
f.close()

invaild_ID_sum = 0
for single_range in ranges:
    start, end = single_range.split("-")
    
    for num in range(int(start),int(end)+1):
        str_num = str(num)
        length = len(str_num)
        
        # Only Even digits can have double digit
        if length %2 == 0:
            mid = length // 2
            
            if str_num[:mid] == str_num[mid:]:
                invaild_ID_sum += num
                
print(invaild_ID_sum)