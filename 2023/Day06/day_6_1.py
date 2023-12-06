import re


f = open("day_6_input.txt","r")
t_line = f.readline()
t_record = re.findall(r'\d+',t_line)
d_line = f.readline()
d_record = re.findall(r'\d+',d_line)
f.close()

win_chance = 1

for i in range(len(t_record)):
    r_time = int(t_record[i])
    r_distance = int(d_record[i])
    win_sum = 0
    
    for j in range(r_time):
        c_speed = j+1
        c_time = r_time - c_speed
        c_distance = c_speed * c_time
        
        if c_distance > r_distance:
            win_sum += 1
            
    win_chance *= win_sum
        

print(win_chance)
    