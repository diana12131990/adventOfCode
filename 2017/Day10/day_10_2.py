import re

f = open("day_10_input.txt","r")

line = f.readline()
line = line.strip()
twist_list = [ord(x) for x in line] + [17,31,73,47,23]
f.close()

numbers = [i for i in range(256)]
skip_size = 0
i = 0
for r in range(64):
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

hex_list = []
for x in range(256/16):
    xor_result = -1
    for i in range(16):
        if i == 0:
            xor_result = numbers[i+16*x]
        else:
            xor_result ^= numbers[i+16*x]
    hex_n = hex(xor_result)
    hex_n = hex_n.replace("0x","")
    if len(hex_n)==1:
        hex_n = "0"+hex_n
    hex_list.append(hex_n)    

print(''.join(hex_list))