import re


f = open("day_6_input.txt","r")
t_line = f.readline()
t_line = t_line.replace(" ","")
t_record = re.findall(r'\d+',t_line)
t_record = int(t_record[0])

d_line = f.readline()
d_line = d_line.replace(" ","")
d_record = re.findall(r'\d+',d_line)
d_record = int(d_record[0])

f.close()


win_chance = 1
win_sum = 0
    
for j in range(t_record):
        c_speed = j+1
        c_time = t_record - c_speed
        c_distance = c_speed * c_time
        
        if c_distance > d_record:
                win_sum += 1
            
win_chance *= win_sum
        

print(win_chance)
    