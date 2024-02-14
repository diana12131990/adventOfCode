import re

f = open("day_10_input.txt","r")

line = f.readline()
line = line.strip()
numbers = re.findall("\d+",line)
twist_list = [int(x) for x in numbers]
f.close()


numbers = [i for i in range(256)]
skip_size = 0
i = 0
for n in twist_list:
    if n != 0:
        i += skip_size
        i = i%256
        j = i+n
        j = j%256
        if j > i:
            twist = numbers[i:j]
        elif j <= i:
            twist = numbers[i:]+numbers[:j]
        twist.reverse()
        for index in range(len(twist)):
            k = i+index
            k = k%256
            numbers[k] = twist[index]
        i += n-1
        
    skip_size += 1
    

print(numbers[0]*numbers[1])