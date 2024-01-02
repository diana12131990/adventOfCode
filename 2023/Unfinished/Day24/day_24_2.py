import re

f = open("day_24_input.txt","r")

haristones = []
for line in f:
    line = line.strip()
    pos,vel = re.split(" @ ",line)
    pos = re.split(", ",pos)
    pos = [float(x)/10**10 for x in pos]
    vel = re.split(", ",vel)
    vel = [int(x) for x in vel]
    haristones.append([pos,vel])
f.close()

def lineLineIntersection(line_1,line_2):
    # line_1 represented as a1x + b1y = c1
    a1 = line_1[1][1]
    b1 = -1 * line_1[1][0]
    c1 = a1*(line_1[0][0]) + b1*(line_1[0][1])
 
    # line_2 represented as a2x + b2y = c2
    a2 = line_2[1][1]
    b2 = -1 * line_2[1][0]
    c2 = a2*(line_2[0][0]) + b2*(line_2[0][1])
 
    determinant = a1*b2 - a2*b1
 
    if (determinant == 0):
        # The lines are parallel. This is simplified
        return False
    else:
        x = (b2*c1 - b1*c2)/determinant
        y = (a1*c2 - a2*c1)/determinant
        t1 = (x - line_1[0][0])/line_1[1][0]
        t2 = (x - line_2[0][0])/line_2[1][0]
        return 20000<=x<=40000 and 20000<=y<=40000 and t1 >= 0 and t2 >= 0
    
intersect_amount = 0
for i in range(len(haristones)-1):
    for j_range in range(len(haristones)-i-1):
        j = i + j_range + 1
        isIntersected = lineLineIntersection(haristones[i],haristones[j])
        if isIntersected:
            intersect_amount += 1
print(intersect_amount)