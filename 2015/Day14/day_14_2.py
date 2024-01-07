import re

f = open("day_14_input.txt","r")

reindeers = {}
for line in f:
    line = line.strip()
    name, line = re.split(" can fly ",line)
    numbers = re.findall("\d+",line)
    
    reindeers.update({name:{"speed":int(numbers[0]),"fly_t":int(numbers[1]),"rest_t":int(numbers[2]),"score":0}})
        
f.close()


for i in range(2503):
    sec = i + 1
    distances = {}
    max_distance = 0
    for r in reindeers:
        speed = reindeers[r]["speed"]
        fly_t = reindeers[r]["fly_t"]
        rest_t = reindeers[r]["rest_t"]
        loop_count = sec/(fly_t+rest_t)
        remain_sec = sec%(fly_t+rest_t)
        
        current_distance = speed*fly_t*loop_count
        if remain_sec <= fly_t:
            current_distance += speed*remain_sec
        else:
            current_distance += speed*fly_t
        
        distances.update({r:current_distance})
        if current_distance > max_distance:
            max_distance = current_distance
    for r in reindeers:
        if distances[r] == max_distance:
            score = reindeers[r]["score"] + 1
            reindeers[r]["score"] = score

max_score = 0
for r in reindeers:
    if reindeers[r]["score"] > max_score:
        max_score = reindeers[r]["score"]
print(max_score)