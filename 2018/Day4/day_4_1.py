import re

f = open("day_4_input.txt","r")

record_list = []
for line in f:
    line = line.strip()
    record_list.append(line)
f.close()

record_list.sort()

guard_record = {}
sleep_min = -1
wake_min = -1
current_guard = -1
for line in record_list:
    time, text = line.split(']', 1)
    time = time[1:]
    text = text.strip()
    
    if "Guard" in text:
        guard_id = re.findall(r'\d+', text)
        current_guard = int(guard_id[0])
        if current_guard not in guard_record:
            guard_record[current_guard] = [0] * 61
            
    else:
        time = re.findall(r'\d+', time)
        if "falls" in text:
            sleep_min = int(time[-1])
            
        elif "wakes" in text:
            wake_min = int(time[-1])
            if sleep_min > wake_min:
                guard_record[current_guard][60] += 60 + wake_min - sleep_min
                for i in range(sleep_min,60):
                    guard_record[current_guard][i] += 1
                for i in range(0,wake_min+1):
                    guard_record[current_guard][i] += 1
            else:
                guard_record[current_guard][60] += wake_min - sleep_min
                for i in range(sleep_min,wake_min):
                    guard_record[current_guard][i] += 1
                    
most_sleep_min = -1
most_sleep_id = -1
for p in guard_record:
    if guard_record[p][60] > most_sleep_min:
        most_sleep_min = guard_record[p][60]
        most_sleep_id = p
        
record = guard_record[most_sleep_id][:-1]
max_minute = record.index(max(record))

print(most_sleep_id*max_minute)