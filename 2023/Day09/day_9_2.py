import re

f = open("day_9_input.txt","r")

total = 0

for line in f:
    line = line.strip()
    
    report = {}
    index = 0
    c_report = re.split(" ",line)
    report.update({index:[int(x) for x in c_report]})
    
    res = False
    while not res:
        l_num = None
        c_report = []
        for c_num in report[index]:
            if l_num != None:
                new_num = c_num - l_num
                c_report.append(new_num)
            l_num = c_num
        
        diff = c_report[0]
        index += 1
        res = all(x == diff for x in c_report)
        if not res:
            report.update({index:c_report})
         
    for i in reversed(range(index)):
        last_value = report[i][0]-diff
        diff = last_value
    
    total += last_value
    
f.close()

print(total)