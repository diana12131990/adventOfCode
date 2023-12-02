import re

f = open("day_1_input.txt","r")
sum = 0

for line in f:
    digits = re.findall(r'\d',line)
    num = int( str(digits[0]) + str(digits[-1]) )
    sum += num

print(sum)
f.close()