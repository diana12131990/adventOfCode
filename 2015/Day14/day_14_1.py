import re

f = open("day_14_input.txt","r")

reindeers = []
for line in f:
    line = line.strip()
    numbers = re.findall("\d+",line)
    numbers = [int(x) for x in numbers]
    
    # 0: speed, 1: fly time, 2: rest time
    reindeers.append(numbers)
        
f.close()
total_sec = 2503
max_distance = 0
for r in reindeers:
    loop_count = total_sec/(r[1]+r[2])
    remain_sec = total_sec%(r[1]+r[2])
    
    current_distance = r[0]*r[1]*loop_count
    if remain_sec <= r[1]:
        current_distance += r[0]*remain_sec
    else:
        current_distance += r[0]*r[1]
    
    if current_distance > max_distance:
        max_distance = current_distance
print(max_distance)