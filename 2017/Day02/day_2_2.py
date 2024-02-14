import re

f = open("day_2_input.txt","r")

total = 0
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    numbers = [int(x) for x in numbers]
    numbers.sort(reverse=True)
    
    for i in range(len(numbers)-1):
        x = numbers[i]
        Found = False
        for j in range(i+1,len(numbers)):
            y = numbers[j]
            print(x,y)
            if x%y == 0:
                print(x/y)
                Found = False
                total += x/y
                break
        if Found:
            break
            
    
print(total)
f.close()